import telebot
from telebot import types
import logging

from telebot.types import Message

from settings import phtsetings
import sqlite3
import time
from rega import registration

from settings import phtsetings
import kb
from gorod import gorodhd

menu = True
kd = False

# bot = telebot.TeleBot('6970053055:AAGp8_DivHfDSkckYW3o7qicvCz7ihbji74')
logger = logging.getLogger(__name__)


def check_narushenie(user_id):
    connection = sqlite3.connect('BaseUsersy.db')
    cursor = connection.cursor()

    cursor.execute('SELECT narush FROM Dostups WHERE telegram_id_for_dostups = ?', (user_id,))
    narushing = cursor.fetchone()

    connection.close()

    if narushing:
        return narushing[0] >= 1  # Вернуть True, если нарушение >= 1, иначе False
    return False


# Технические переменные

hnya = 23
Nepovtorka = False


def handle_admin(message: Message, bot):
    admin_id = 792451145
    bot.send_message(chat_id=admin_id, text=message.text)


def handle_statusmykt(message):
    if not check_narushenie(message.chat.id):
        kb.handle_status(message)

    else:
        message.send_message(message.chat.id, 'ВАШ АКАУНТ ЗАБАНЕН')


def handle_start(message):
    if not check_narushenie(message.chat.id):
        kb.ifingstart(message)

    else:
        message.send_message(message.chat.id, 'ВАШ АКАУНТ ЗАБАНЕН')


def handle_escape(message):
    if not check_narushenie(message.chat.id):
        kb.handle_menuh(message)

    else:
        message.send_message(message.chat.id, 'ВАШ АКАУНТ ЗАБАНЕН')


def handle_settings(message):
    if not check_narushenie(message.chat.id):
        phtsetings.handle_settings(message)

    else:
        message.send_message(message.chat.id, 'ВАШ АКАУНТ ЗАБАНЕН')


def handle_text(message):
    if not check_narushenie(message.chat.id):
        global kd
        if message.text == 'Начать игру!':

            kb.handle_text_1(message)

        elif message.text == 'Да, я готов.':

            kb.handle_text_1(message)
        elif message.text == 'Оплатить абонемент':
            gorodhd.info_buy_abonem(message)

        elif message.text.startswith('КуА/'):
            crb = message.text[len('КуА/'):].lstrip()
            if crb:
                crbi = int(crb)
                gorodhd.buyng_abonement(message)
            else:
                print("Строка после 'КуА/' пуста.")


        elif message.text == 'Переход к главному меню':
            if menu == True:

                kb.handle_menuh(message)

            else:
                message.send_message(message.from_user.id, 'С этого места нельзя вызвать меню.')

        elif message.text == 'Получить реферальную ссылку':
            kb.ref(message)


        # Лока город
        elif message.text == 'Городок':
            if menu == True:

                gorodhd.handle_text_gorod(message)

            else:
                message.send_message(message.from_user.id, 'Неа, нельзя.')

        elif message.text == 'Карта':
            if menu == True:

                gorodhd.handle_map(message)

            else:
                message.send_message(message.from_user.id, 'Запрещено')
        elif message.text == 'Ул. Свободы':

            gorodhd.handle_ul_svobodi(message)


        elif message.text == 'Ул. Культивирования':

            gorodhd.ul_kult(message)


        elif message.text == 'Начать культивировать':
            if kd == False:
                kd = True
                gorodhd.start_kul(message)

                kd = False
            elif kd == True:
                message.send_message(message.from_user.id, 'Дождитесь окончания культивации')
            else:
                pass



        # Лицензия и тд
        elif message.text == 'Принимаю условия':
            kb.licenceyesorno(message)
        elif message.text == 'Не принимаю условия':
            kb.banningstart(message)
            time.sleep(30.0)
            check_narushenie(message.chat.id)


        elif message.text == 'BG':

            gorodhd.handle_bg(message)

            message.send_message(message.from_user.id, 'Вы культивируете.')
        elif message.text == 'BM':

            gorodhd.handle_bm(message)

            message.send_message(message.from_user.id, 'Вы культивируете.')

        elif message.text == 'BK':

            gorodhd.handle_bk(message)




        elif message.text == 'Клановая улица':
            message.send_message(message.from_user.id, 'Разработка идет полным ходом.')



        # Настройки

        elif message.text == 'Отключить картинки':
            phtsetings.handle_nophotos(message)
        elif message.text == 'Включить картинки':
            phtsetings.handle_onphotos(message)
        elif message.text == 'Получить реферальную ссылку':
            phtsetings.handle_ref(message)


def main():
    bot = telebot.TeleBot('6543582452:AAE3UAvbbJyN1n8hVmhvbyArX3DANS5Nsko')

    logging.basicConfig(
        level=logging.DEBUG,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")

    bot.register_message_handler(
        callback=lambda message: handle_admin(message, bot), func=lambda message: message.text.find('@admin') != -1)

    bot.register_message_handler(callback=handle_statusmykt, commands=['statusmykt'])
    bot.register_message_handler(callback=handle_start, commands=['start'])
    bot.register_message_handler(callback=handle_escape, commands=['escape'])
    bot.register_message_handler(callback=handle_settings, commands=['settings'])

    bot.register_message_handler(callback=kb.handle_status, commands=['statusmykt'])
    bot.register_message_handler(callback=handle_text, func=lambda message: True)

    # Kb.py
    # bot.register_message_handler(callback=kb.handle_menuh, func=lambda message: True)
    # bot.register_message_handler(callback=kb.handle_text_1, func=lambda message: True)
    # bot.register_message_handler(callback=kb.licenceyesorno, func=lambda message: True)
    # bot.register_message_handler(callback=kb.handle_reg, func=lambda message: True)

    try:
        bot.polling(none_stop=True)
    except:
        logger.error("Bot stopped!")
        bot.close()


if __name__ == '__main__':
    main()
