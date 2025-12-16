import telebot
from flask import Flask, request
import os

# --- কনফিগারেশন ---
# আপনার বটের টোকেন
BOT_TOKEN = '7989187794:AAHqkiTZk8jCC3E4pxZgmFTSLlYy5BRlCDM'
bot = telebot.TeleBot(BOT_TOKEN)

# ফ্লাস্ক সার্ভার সেটআপ
app = Flask(__name__)

# --- রুট পেজ (সার্ভার চেক করার জন্য) ---
@app.route('/')
def index():
    return "Bot is running perfectly on Render!", 200

# --- ওয়েবহুক রিসিভার ---
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return '', 200
    else:
        return 'Error', 403

# --- বটের কমান্ড ---
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "হ্যালো! আমি সফলভাবে কাজ করছি। নতুন সার্ভারে স্বাগতম!")

# --- সার্ভার রান করা ---
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
