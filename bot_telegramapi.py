import telebot
from telebot import types
from bot_answers import answers, keys

token = r"1387124174:AAFAUEBUjYFgTaryNCTpgPsnQmvP0lbYqlM" # @Shaganetestbot
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} ты написал мне /start')


@bot.message_handler(content_types=['text']) 
def get_text_messages(message): 
    if message.text.lower() == 'привет':
        keyboard = types.InlineKeyboardMarkup()
        for key_name in keys:
            key = types.InlineKeyboardButton(text=key_name[0], callback_data=key_name[1])
            keyboard.add(key)
        bot.send_message(message.from_user.id, answers['привет'].format(message.from_user.first_name), reply_markup=keyboard)
    
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAPMX5h6smjS3MoOM7KxfF0RCLtDBBwAApQDAAJHFWgJhy6ChFrKX5UbBA')
        bot.send_message(message.from_user.id, 'Are you crazy?')

    elif message.text.lower() == '/menu':
        keyboard_menu = types.ReplyKeyboardMarkup(True, True)
        keyboard_menu.row('Италия', 'Франция', 'Армения', 'Грузия', 'ХЗ')
        bot.send_message(message.chat.id, 'Вот тебе меню', reply_markup=keyboard_menu)

    elif message.text.lower() in answers: 
        bot.send_message(message.from_user.id, answers[message.text.lower()])

    else: 
        bot.send_message(message.from_user.id, "Я тебя не понимаю.\nНапиши что-нибудь, например /help или 'Я тебя люблю'\nМожно вызвать /menu")
    
@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    bot.send_message(message.from_user.id, "Я тоже так могу! Смотри")
    bot.send_sticker(message.from_user.id, message.json['sticker']['file_id'])

bot.polling(none_stop=True, interval=0)