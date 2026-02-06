import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot('8348577528:AAESO9fG1T_iEtG3bF544eBG9SsrJy9FSkk')

# ဘာသာစကား ရွေးချယ်ရန် Keyboard
def language_markup():
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("🇲🇲 မြန်မာစာ", callback_data="lang_mm"),
        InlineKeyboardButton("🇺🇸 English", callback_data="lang_en")
    )
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id, 
        "Please select your language / ဘာသာစကားရွေးချယ်ပေးပါ ✨", 
        reply_markup=language_markup()
    )

# ခလုတ်နှိပ်လိုက်တဲ့အခါ တုံ့ပြန်ပုံ
@bot.callback_query_handler(func=lambda call: call.data.startswith('lang_'))
def set_language(call):
    if call.data == "lang_mm":
        bot.answer_callback_query(call.id, "မြန်မာဘာသာကို ရွေးချယ်လိုက်ပါပြီ")
        bot.edit_message_text("တွက်ချက်မည့် ဂဏန်းများကို ပို့ပေးပါဗျ။ 🧮", call.message.chat.id, call.message.message_id)
    else:
        bot.answer_callback_query(call.id, "English language selected")
        bot.edit_message_text("Please send the numbers you want to calculate. 🧮", call.message.chat.id, call.message.message_id)

@bot.message_handler(func=lambda message: True)
def calculate(message):
    try:
        result = eval(message.text)
        bot.reply_to(message, f"✅ Result: {result}")
    except:
        bot.reply_to(message, "⚠️ Invalid input! Please send numbers only.")

bot.infinity_polling()
