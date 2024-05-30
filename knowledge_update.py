from poe_api_wrapper import PoeApi
import configparser

config = configparser.RawConfigParser()
config.read('secrets.ini')

# Read knowledgeSourceId and title from config.ini
knowledge_config = configparser.ConfigParser()
knowledge_config.read('config.ini')
knowledgeSourceId = knowledge_config.getint('Bot', 'KnowledgeSourceId')
KnowledgeSourceTitle = knowledge_config.get('Bot', 'KnowledgeSourceTitle')

with open('harvest/know_base/txt/job_list.txt', 'r', encoding='utf-8') as f:
    data = f.read()

tokens = {
    'b': config.get('Tokens', 'b'),
    'lat': config.get('Tokens', 'lat')
}

client = PoeApi(cookie=tokens)

bot = config.get('Bot', 'bot_name')

print(client.get_available_knowledge(botName=bot, get_all=True))

# edit [bot] section in secrets.ini with the correct knowledgeSourceId and KnowledgeSourceTitle
'''
client.edit_knowledge(knowledgeSourceId=knowledgeSourceId,
                      title=KnowledgeSourceTitle, content=data)
'''
