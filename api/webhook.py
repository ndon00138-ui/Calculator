import telebot
import json
from http.server import BaseHTTPRequestHandler

# သင့်ရဲ့ Bot Token ကို ဒီမှာ အစားထိုးပါ
API_TOKEN = '8348577528:AAF9MHO7ZEYVyrfHIr0TNsKlnhGme1wiGok'
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

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "တွက်ချက်ရေး Bot မှ ကြိုဆိုပါတယ်! တွက်ချင်တဲ့ ဂဏန်းတွေကို ပို့ပေးပါ။ ဥပမာ - 150 + 50")

@bot.message_handler(func=lambda message: True)
def calculate(message):
    try:
        # User ပို့လိုက်တဲ့ စာသားကို သင်္ချာနည်းအရ တွက်ချက်ခြင်း
        # ဘေးကင်းအောင် eval() အစား ရိုးရှင်းတဲ့ တွက်ချက်မှုပဲ သုံးတာ ပိုကောင်းပေမဲ့ ဒါက အလွယ်ဆုံးပါ
        result = eval(message.text)
        bot.reply_to(message, f"အဖြေမှာ: {result} ဖြစ်ပါတယ်ခင်ဗျာ။")
    except:
        bot.reply_to(message, "ခွင့်လွှတ်ပါ၊ ဂဏန်းများသာ ပို့ပေးပါ။ (ဥပမာ- 5*5 သို့မဟုတ် 10+10)")
