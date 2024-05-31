import re
from flask import Response
import configparser
from requests.exceptions import ConnectionError
from flask import Flask, request, render_template, Response, stream_with_context
from flask_cors import CORS
from poe_api_wrapper import PoeApi
import traceback
import json


# ------------------ SETUP ------------------


app = Flask(__name__)

config = configparser.RawConfigParser()
config.read('secrets.ini')

tokens = {
    'b': config.get('Tokens', 'b'),
    'lat': config.get('Tokens', 'lat')
}

client = PoeApi(cookie=tokens)

bot = config.get('Bot', 'bot_name')

cors = CORS(app)


@app.route("/")
def home():
    return render_template("index.html")


# ------------------ EXCEPTION HANDLERS ------------------

# Sends response back to Deep Chat using the Response format:
# https://deepchat.dev/docs/connect/#Response


@app.errorhandler(Exception)
def handle_exception(e):
    print(traceback.format_exc())
    return {"error": str(e)}, 500

# ------------------ POE API ------------------

# *****************without streaming*****************


@app.route("/chat", methods=["POST"])
def chat():
    body = request.json
    messages = body.get('messages')
    if messages is None or len(messages) == 0:
        return {"error": "No message provided"}, 400
    message = messages[0].get('text')
    print(f"Received message: {message}")  # print the received message
    if message is None:
        return {"error": "No message provided"}, 400
    message = str(message)  # convert message to string
    for chunk in client.send_message(bot, message):
        pass
    # DEBUG print(chunk["text"])
    return {"text": chunk["text"]}

# *****************with streaming*****************


@app.route("/chat-stream", methods=["POST"])
def chat_stream():
    body = request.json
    messages = body.get('messages')
    if messages is None or len(messages) == 0:
        return Response(json.dumps({"error": "No message provided"}), 400)
    message = messages[0].get('text')
    print(f"Received message: {message}")  # print the received message
    if message is None:
        return Response(json.dumps({"error": "No message provided"}), 400)
    message = str(message)  # convert message to string

    def generate():
        for i, chunk in enumerate(client.send_message(bot, message)):
            # Convert Markdown links to HTML links
            chunk_text = re.sub(r"\[(.*?)\]\((.*?)\)",
                                r'<a href="\2">\1</a>', chunk["text"])

            # Convert Markdown lists to HTML lists
            chunk_text = re.sub(
                r"\n\* (.*?)\n", r'<ul><li>\1</li></ul>', chunk_text)
            chunk_text = re.sub(
                r"\n\- (.*?)\n", r'<ul><li>\1</li></ul>', chunk_text)

            # Add the 'overwrite' property to the messages
            yield 'data: %s\n\n' % json.dumps({'html': '<p>' + chunk_text + '</p>', 'overwrite': 'True'})

    return Response(generate(), mimetype='text/event-stream')


if __name__ == "__main__":
    app.run(port=7890)
