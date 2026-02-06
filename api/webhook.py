import telebot
import json
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from http.server import BaseHTTPRequestHandler

# သင့်ရဲ့ Token အသစ်
API_TOKEN = '8348577528:AAESO9fG1T_iEtG3bF544eBG9SsrJy9FSkk'
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
    # သင်ပေးထားတဲ့ Netlify Link ကို ထည့်ထားပေးပါတယ်
    open_btn = InlineKeyboardButton(text="🌐 Open Website 🚀", url="https://5-4.netlify.app")
    markup.add(open_btn)
    
    bot.send_message(
        message.chat.id, 
        "မင်္ဂလာပါ! ကျွန်တော်က Calculator Bot ပါ။\nဂဏန်းတွက်ချက်မှုများ ပို့ပေးနိုင်ပါတယ်ခင်ဗျာ။ ✨", 
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: True)
def calculate(message):
    try:
        # သင်္ချာတွက်ချက်ခြင်း
        result = eval(message.text)
        
        markup = InlineKeyboardMarkup()
        btn = InlineKeyboardButton(text="🔎 website သုံးရန်", url="https://5-4.netlify.app")
        markup.add(btn)
        
        bot.reply_to(message, f"✅ အဖြေမှာ: {result} ဖြစ်ပါတယ်", reply_markup=markup)
    except:
        bot.reply_to(message, "❌ ဂဏန်းများသာ ပို့ပေးပါ (ဥပမာ- 12+5)")
