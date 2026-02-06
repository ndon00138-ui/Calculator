import telebot
import json
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from http.server import BaseHTTPRequestHandler

API_TOKEN = '8348577528:AAFiCxaKYhUvNUgCQ4vcpVuSxZpv4cqIGss'
bot = telebot.TeleBot(API_TOKEN, threaded=False)

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        update = telebot.types.Update.de_json(post_data.decode('utf-8'))
        bot.process_new_updates([update])
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"status": "ok"}).encode())

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("🇲🇲 မြန်မာ", callback_data="mm"),
        InlineKeyboardButton("🇺🇸 English", callback_data="en")
    )
    bot.send_message(message.chat.id, "Select Language / ဘာသာစကားရွေးပါ", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "mm":
        bot.answer_callback_query(call.id, "မြန်မာစာ ရွေးချယ်ပြီး")
        bot.send_message(call.message.chat.id, "ဂဏန်းများ ပို့ပေးပါဗျ။")
    elif call.data == "en":
        bot.answer_callback_query(call.id, "English selected")
        bot.send_message(call.message.chat.id, "Please send numbers.")

@bot.message_handler(func=lambda message: True)
def calculate(message):
    try:
        result = eval(message.text)
        bot.reply_to(message, f"Result: {result}")
    except:
        bot.reply_to(message, "Error!")
