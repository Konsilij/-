import sqlite3
import time
import telebot
from telebot import types

bot = telebot.TeleBot('6970053055:AAGp8_DivHfDSkckYW3o7qicvCz7ihbji74')

#Переменная для отключения и включения фоток
onpht = 1
offpht = 0




@bot.message_handler(func=lambda message: True)
def handle_settings(message):
    
    connection = sqlite3.connect('BaseUsersy.db')
    cursor = connection.cursor()
    cursor.execute('SELECT photos FROM Users WHERE chat_id = ?', (message.chat.id,))
    photons = cursor.fetchone()
    photoks = photons[0]
    connection.commit()
    connection.close()
    if photoks <= 0:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Включить картинки")
        btn2 = types.KeyboardButton("Получить реферальную ссылку")
        
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, '_*Возможные настройки:*_', reply_markup=markup, parse_mode='Markdown')
    elif photoks >= 1:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Отключить картинки")
        btn2 = types.KeyboardButton("Получить реферальную ссылку")
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, '_*Возможные настройки:*_', reply_markup=markup, parse_mode='Markdown')


@bot.message_handler(func=lambda message: True)
def handle_nophotos(message):
    connection = sqlite3.connect('BaseUsersy.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE Users SET photos = ? WHERE chat_id = ?', (offpht, message.chat.id,))
    connection.commit()
    connection.close()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Включить картинки")
        
    markup.add(btn1)
    bot.send_message(message.from_user.id, '_*Картинки отключены*_', reply_markup=markup, parse_mode='Markdown')
    
@bot.message_handler(func=lambda message: True)
def handle_onphotos(message):
    connection = sqlite3.connect('BaseUsersy.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE Users SET photos = ? WHERE chat_id = ?', (onpht, message.chat.id,))
    connection.commit()
    connection.close()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Отключить картинки")
    markup.add(btn1)
    bot.send_message(message.from_user.id, '_*Картинки включены*_', reply_markup=markup, parse_mode='Markdown')





















    
