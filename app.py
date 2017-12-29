from flask import Flask, request
import telepot
import urllib3
import random, string
import os

print("Starting KawaiiBot")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-'
secret = ''.join(random.choice(chars) for i in range(random.randint(32, 64)))
bot = telepot.Bot(os.environ['BOT_TOKEN'])
bot.setWebhook("https://kawaiicentral-bot.herokuapp.com/{}".format(secret), max_connections=1)

app = Flask(__name__)

@app.route('/{}'.format(secret), methods=["POST"])
def telegram_webhook():
    update = request.get_json()
    print(update)
    if "message" in update:
        text = update["message"]["text"]
        chat_id = update["message"]["chat"]["id"]
        bot.sendMessage(chat_id, "From the web: you said '{}'".format(text))
    return "OK"

if __name__ == "__main__":
    app.run()
