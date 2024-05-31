# AiChatBridge
 
![Untitled design](https://github.com/TheLime1/AiChatBridge/assets/47940043/5f81fe22-1fcf-4408-9207-857d144322d6)

## Introduction
This tutorial will guide you through the process of integrating your Poe.com bot into your website. By the end of this tutorial, you'll have a fully functional bot integrated into your site with a custom front-end, ready to interact with your visitors.

---

[before we begin use this template repo](https://github.com/TheLime1/AiChatBridge)

![template repo](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/0wdl7rbeti3h3zrvqsot.png)

and dont forget to install the librearies :

```
 pip install -r requirements.txt
```


---

## Step 1: Get the Cookies from quora.com
First things first, you'll need to grab some cookies.They are essential for your bot's authentication and functionality. Here's how to get them:

1. **Log in to quora.com:** Open your web browser and navigate to Poe.com. Log in with your account credentials.

2. **Open Developer Tools:** Once logged in, open the developer tools in your browser. You can do this by right-clicking on the page and selecting "Inspect" or pressing Ctrl+Shift+I (Windows/Linux) or Cmd+Option+I (Mac).

3. **Navigate to the Application Tab:** In the developer tools window, go to the "Application" tab. 

4. **Locate the Cookies Section:** Under the "Storage" section on the left sidebar, click on "Cookies" and select https://quora.com from the dropdown.

5. **Copy the Cookies:** Find the cookies **<u>(m-b and m-lat)</u>**, right-click on them, and select "Copy". Open your text editor and paste the cookies into `secrets.ini` .

```
[Tokens]
b = XXXXXXXXXXXXXXXXXXX==
lat = XXXXXXXXXXXXXXXXXX==
```

![coockies](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/n8g1q4oghsv3xre86lv1.png)

---

## Step 2: Create Your Bot in Poe.com 

With the cookies saved, it's time to create your bot.

**<u>Make sure you have logged in poe.com using the same email which registered on quora.com.</u>**

Follow these steps:

1. **Navigate to the Bot Creation Page:** On Poe.com, find the "Create Bot" section. This is usually located in your account dashboard.
![create bot](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/k4e0xksww5ufkiy30mhe.png)

2. **Set Up Your Bot:** Fill in the necessary details for your bot, such as its name, description, and any specific functionalities you want it to have. Don't forget to upload an avatar to give your bot some personality! 
![bot form](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/t70qwcdokwtnvlhime48.png)

3. **Save and Deploy:** Once you've configured your bot, click on the "Save" button to finalize the creation process. Your bot is now live and ready to be integrated into your website.

4.  **Add bot name** to `secrets.ini`
```
[Bot]
bot_name = 5ademni_bot
```

---

## Step 3: Deploy!

- Run `app.py`

![native chatbot](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/3gzayzrmseanz0gdprkl.png)

- integrate with your website using `<iframe>`


![chatbot integration](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zab3y0y1179pafudhja2.png)

---

## Bonus Step: Knowledge Base!


![Knowledge Base](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/37r72c3ec27gs74oc7n3.png)

You can automate editing your bot knowledge base using `knowledge_update.py`.
### example :
this bot gets updates daily using [scraped data](https://raw.githubusercontent.com/5ademni/job-scraper/main/harvest/know_base/json/tanit_informatique.json) for joblistings, using Github Actions 

![github actions](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/27kzztj400br8xqisxvd.png)

## Thats it!
you can follow me on [Github](https://github.com/TheLime1) if you are interested About APIs and Ai !

- [template repo](https://github.com/TheLime1/AiChatBridge)
- [bot used in this demo](https://poe.com/5ademni_bot)

### You can read these docs if you want to further customize the chatbot
- [Chat UI](https://github.com/OvidijusParsiunas/deep-chat)
- [Poe API](https://github.com/snowby666/poe-api-wrapper)

 


