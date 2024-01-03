import sqlite3
import time
import telebot
from telebot import types




bot = telebot.TeleBot('6970053055:AAGp8_DivHfDSkckYW3o7qicvCz7ihbji74')

#Технические переменные

hnya = 23
Nepovtorka = False

bg = True
bm = True
bk = True


LHT = False
LMT = False
BKT = False
PBT = False





@bot.message_handler(func=lambda message: True)
def handle_text_gorod(message):
    
    global hnya
    if message.text == 'Городок':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Карта")
        btn2 = types.KeyboardButton("Соседи")
        
        btn4 = types.KeyboardButton("Конедром")
        btnm = types.KeyboardButton("BM")
        markup.add(btn1, btn2, btn4, btnm)
        bot.send_message(message.from_user.id, 'Город он такой, городской, даже если средневековый.', reply_markup=markup)
    




#Обработчик улицы свободы

@bot.message_handler(func=lambda message: True)
def handle_ul_svobodi(message):
    global LHT
    global LMT
    global BKT
    global PBT
   
    connection = sqlite3.connect('BaseUsersy.db')
    cursor = connection.cursor()
    cursor.execute('SELECT vinos FROM Users WHERE chat_id = ?', (message.chat.id,))
    momentvinos = cursor.fetchone()
    
    connection.commit()
    connection.close()   

    
    if momentvinos is not None:
        vn = momentvinos[0]
        
    elif momentvinos is None:
        print("Произошла ошибка. Код ошибки: SOMEWithULSvobodi/Line 68 gorodhd . Ид игрока и его имя: " + str(message.chat.id) + str(message.from_user.first_name))
        bot.send_message(message.chat.id, 'Обратитесь к Администрации проекта. Код ошибки: SOMEWithULSvobodi/Line 68 gorodhd')
        vn = 0

    else:
        pass


    




    
        
        
    


    if vn >= 1:    
#Функционал

        connection = sqlite3.connect('BaseUsersy.db')
        cursor = connection.cursor()
        cursor.execute('SELECT LH FROM DpULSvobodi WHERE chat_id = ?', (message.chat.id,))
        LHUS = cursor.fetchone()
        LH = LHUS[0]
        connection.commit()
        connection.close()

        if LH == 1:
            LHT = True
        else:
            pass
            



        connection = sqlite3.connect('BaseUsersy.db')
        cursor = connection.cursor()
        cursor.execute('SELECT LM FROM DpULSvobodi WHERE chat_id = ?', (message.chat.id,))
        LMUS = cursor.fetchone()
        LM = LMUS[0]
        connection.commit()
        connection.close()

        if LM == 1:
            LMT = True
        else:
            pass




        connection = sqlite3.connect('BaseUsersy.db')
        cursor = connection.cursor()
        cursor.execute('SELECT BK FROM DpULSvobodi WHERE chat_id = ?', (message.chat.id,))
        BKUS = cursor.fetchone()
        BK = BKUS[0]
        connection.commit()
        connection.close()

        if BK == 1:
            BKT = True
        else:
            pass




        connection = sqlite3.connect('BaseUsersy.db')
        cursor = connection.cursor()
        cursor.execute('SELECT PodpolBoi FROM DpULSvobodi WHERE chat_id = ?', (message.chat.id,))
        PDUS = cursor.fetchone()
        PB = PDUS[0]
        connection.commit()
        connection.close()

        if PB == 1:
            PBT = True
        else:
            pass

        

        
        if LHT == True:
            vn -= 1
            connection = sqlite3.connect('BaseUsersy.db')
            cursor = connection.cursor()
            cursor.execute('UPDATE Users SET vinos = ? WHERE chat_id = ?', (vn, message.chat.id,))
            connection.commit()
            connection.close()

            if LMT == True:
                



                if BKT == True:
                    




                    if PBT == True:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                        btn1 = types.KeyboardButton("Лавка Хиппи")
                        btn2 = types.KeyboardButton("Лавка Моргана")
                        btn3 = types.KeyboardButton("Букмекерская контора")
                        btn4 = types.KeyboardButton("Арена подпольных боев")
                        btn8 = types.KeyboardButton("BG")
                        markup.add(btn1, btn2, btn3, btn4, btn8)
                        bot.send_message(message.from_user.id, '- Здраствуйте, Господин. Для вас открыты все двери.', reply_markup=markup)


                    else:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                        btn1 = types.KeyboardButton("Лавка Хиппи")
                        btn2 = types.KeyboardButton("Лавка Моргана")
                        btn3 = types.KeyboardButton("Букмекерская контора")
                        btn4 = types.KeyboardButton("???")
                        btn8 = types.KeyboardButton("BG")
                        markup.add(btn1, btn2, btn3, btn4, btn8)
                        bot.send_message(message.from_user.id, 'Порой люди задумываються - а можешь ли ты быть их братом, которого в детстве просто перепутали?', reply_markup=markup)



                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    btn1 = types.KeyboardButton("Лавка Хиппи")
                    btn2 = types.KeyboardButton("Лавка Моргана")
                    btn3 = types.KeyboardButton("???")
                    btn4 = types.KeyboardButton("???")
                    btn8 = types.KeyboardButton("BG")
                    markup.add(btn1, btn2, btn3, btn4, btn8)
                    bot.send_message(message.from_user.id, 'Тебя не встречают как родного, но хоть не пытаються убить, Уже что-то.', reply_markup=markup)




            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Лавка Хиппи")
                btn2 = types.KeyboardButton("???")
                btn3 = types.KeyboardButton("???")
                btn4 = types.KeyboardButton("???")
                btn8 = types.KeyboardButton("BG")
                markup.add(btn1, btn2, btn3, btn4, btn8)
                bot.send_message(message.from_user.id, 'Недобрые взгляды смотрят тебе в спину... Они тебя недолюбливают.', reply_markup=markup)
        else:
            bot.send_message(message.from_user.id, 'Тебе тут делать нечего, малой')



    else:
        bot.send_message(message.from_user.id, 'Я не могу двигаться, я устал...')
























@bot.message_handler(func=lambda message: True)
def handle_map(message):
    
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Ул. Свободы")
    btn2 = types.KeyboardButton("Ул. Культивирования")
    btn3 = types.KeyboardButton("Ул. Товарная")
    btn4 = types.KeyboardButton("Ул. Девалье")
    btn5 = types.KeyboardButton("Пр. Небесного Пламени")
    btn6 = types.KeyboardButton("Площадь красного креста")
    btn7 = types.KeyboardButton("Запретная улица семи светил.")
    btn8 = types.KeyboardButton("BG")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    bot.send_message(message.from_user.id, 'Отправится на:', reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_bg(message):
    
    if message.text == 'BG':
        if bg == True:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Карта")
            btn2 = types.KeyboardButton("Соседи")
            
            btn4 = types.KeyboardButton("Конедром")
            btnm = types.KeyboardButton("BM")
            markup.add(btn1, btn2, btn4, btnm)
            bot.send_message(message.from_user.id, 'Город он такой, городской, даже если средневековый.', reply_markup=markup)
        else:
            bot.send_message(message.from_user.id, 'С этого места нельзя вернуться в Городок')

def handle_bm(message):
    
    
    if bm == True:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Городок")
        btn2 = types.KeyboardButton("Канцелярия")
        btn3 = types.KeyboardButton("Гостинница")
        btn4 = types.KeyboardButton("Клановая область")
        
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, 'Город он такой, городской, даже если средневековый.', reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, 'С этого места нельзя выйти в главное меню')


@bot.message_handler(func=lambda message: True)
def handle_bk(message):
    
    if message.text == 'BK':
        if bk == True:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
            btn1 = types.KeyboardButton("Ул. Свободы")
            btn2 = types.KeyboardButton("Ул. Культивирования")
            btn3 = types.KeyboardButton("Ул. Товарная")
            btn4 = types.KeyboardButton("Ул. Девалье")
            btn5 = types.KeyboardButton("Пр. Небесного Пламени")
            btn6 = types.KeyboardButton("Площадь красного креста")
            btn7 = types.KeyboardButton("Запретная улица семи светил.")
            btn8 = types.KeyboardButton("BG")
            markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
            bot.send_message(message.from_user.id, 'Отправится на:', reply_markup=markup)
            
            
            
        else:
            bot.send_message(message.from_user.id, 'С этого места нельзя посмотреть карту')


def after_kul(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
    btn1 = types.KeyboardButton("Начать культивировать")
    btn2 = types.KeyboardButton("Оплатить абонемент на одну ссесию")
    btn3 = types.KeyboardButton("Вип зал")
    btn4 = types.KeyboardButton("Дополнительные услуги")
    btn5 = types.KeyboardButton("BK")    
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.from_user.id, 'Вынырнув из прострации, вы поняли что получили 10 ци.', reply_markup=markup)











#УЛИЦА КУЛЬТИВИРОВАНИЯ
def ul_kult(message):
    connection = sqlite3.connect('BaseUsersy.db')
    cursor = connection.cursor()
    cursor.execute('SELECT vinos FROM Users WHERE chat_id = ?', (message.chat.id,))
    momentvinos = cursor.fetchone()
    if momentvinos is None:
        bot.send_message(message.from_user.id, 'Обратитесь к Администрации проекта. Код ошибки: NoRegistredNowInDataBase')
               
        vn = 10
    else:
        vn = momentvinos[0]
        pass
    
    connection.commit()
    connection.close()
    if vn >= 1:
        vn -= 1
        connection = sqlite3.connect('BaseUsersy.db')
        cursor = connection.cursor()
        cursor.execute('UPDATE Users SET vinos = ? WHERE chat_id = ?', (vn, message.chat.id,))
        connection.commit()
        connection.close()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
        btn1 = types.KeyboardButton("Начать культивировать")
        btn2 = types.KeyboardButton("Оплатить абонемент")
        btn3 = types.KeyboardButton("Вип зал")
        btn4 = types.KeyboardButton("Дополнительные услуги")
        btn5 = types.KeyboardButton("BK")    
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, 'Это общественное место для практиков. Здесь за малую плату можно покультивировать, и получить ци.', reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, 'Я не могу двигаться, я устал...')

def start_kul(message):
    connection = sqlite3.connect('BaseUsersy.db')
    cursor = connection.cursor()
    cursor.execute('SELECT abonems FROM Dostups WHERE telegram_id_for_dostups = ?', (message.chat.id,))
    op = cursor.fetchone()
    connection.commit()
    connection.close()
    if op is not None:
        opl = op[0]
    elif op is None:
        bot.send_message(message.from_user.id, 'Обратитесь к Администрации проекта. Код ошибки: NoRegistredNowInDataBase')
        print("Произошла ошибка. Код ошибки: NoRegistredNowInDataBase . Ид игрока и его имя: " + str(message.chat.id) + str(message.from_user.first_name))
        opl = 10000
    else:
        print("something gone wrong")
        
    



    if opl >= 1:
        oplnowi = opl - 1
        connection = sqlite3.connect('BaseUsersy.db')
        cursor = connection.cursor()
        cursor.execute('UPDATE Dostups SET abonems = ? WHERE telegram_id_for_dostups = ?', (oplnowi, message.chat.id,))
        
    
        connection.commit()
        connection.close()
        
        bot.send_message(message.from_user.id, 'Погружаясь в культивацию, вы осознали что возможно вы пробудете в ней несколько больше чем ожидали...')
        time.sleep(260.0)
        connection = sqlite3.connect('BaseUsersy.db')
        cursor = connection.cursor()
        cursor.execute('SELECT tsi FROM Users WHERE chat_id = ?', (message.chat.id,))
        momtsi = cursor.fetchone()
        tsikm = momtsi[0]
        tsik = tsikm + 10
        connection.commit()
        connection.close()
        time.sleep(0.3)
        connection = sqlite3.connect('BaseUsersy.db')
        cursor = connection.cursor()
        cursor.execute('UPDATE Users SET tsi = ? WHERE chat_id = ?', (tsik, message.chat.id,))
        connection.commit()
        connection.close()
        after_kul(message)
    elif opl is None:
        bot.send_message(message.from_user.id, 'Обратитесь к Администрации проекта. Код ошибки: NoRegistredNowInDataBase')
        
    else:
        bot.send_message(message.from_user.id, 'Купите абонемент.')
    





def info_buy_abonem(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
        btn1 = types.KeyboardButton("КуА/1")
        btn2 = types.KeyboardButton("КуА/10")
        btn3 = types.KeyboardButton("КуА/100")
        btn4 = types.KeyboardButton("КуА/1000")
        btn5 = types.KeyboardButton("BK")    
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, 'Вы можете купить абонемент здесь. Стандарт: 10 сеансов за 100 Дублонов. Но вы можете собственноручно подобрать свой абонемент. КуА/И какое-то число.\nПример: КуА/23', reply_markup=markup)


def buyng_abonement(message):
    comam = int(message.text[len('КуА/'):].lstrip())
    costabonem = comam * 10
    connection = sqlite3.connect('BaseUsersy.db')
    cursor = connection.cursor()
    cursor.execute('SELECT money FROM Users WHERE chat_id = ?', (message.chat.id,))
    money_for_abom = cursor.fetchone()
    if money_for_abom is None:
        bot.send_message(message.from_user.id, 'Обратитесь к Администрации проекта. Код ошибки: NoRegistredNowInDataBase')
        nm = 10000
    else:
        nm = money_for_abom[0]
        pass
    
    connection.commit()
    connection.close()
    
    if nm >= costabonem:
        nm -= costabonem
        
        time.sleep(0.2)
        connection = sqlite3.connect('BaseUsersy.db')
        cursor = connection.cursor()
        cursor.execute('UPDATE Users SET money = ? WHERE chat_id = ?', (nm, message.chat.id,))
        
        connection.commit()
        connection.close()
        time.sleep(0.2)
        
        connection = sqlite3.connect('BaseUsersy.db')
        cursor = connection.cursor()
        cursor.execute('SELECT abonems FROM Dostups WHERE telegram_id_for_dostups = ?', (message.chat.id,))
        ab = cursor.fetchone()
        connection.commit()
        connection.close()

        
        if ab == None:
            bot.send_message(message.from_user.id, 'Обратитесь к Администрации проекта. Код ошибки: NoRegistredNowInDataBase')
            abo = 0
        else:
            abo = ab[0]
            pass
        if ab and len(ab) > 0:
            
            
        
            abo += comam
        
        else:
            bot.send_message(message.from_user.id, 'Обратитесь к Администрации проекта. Код ошибки: NoRegistredNowInDataBase')

        connection = sqlite3.connect('BaseUsersy.db')
        cursor = connection.cursor()
        cursor.execute('UPDATE Dostups SET abonems = ? WHERE telegram_id_for_dostups = ?', (abo, message.chat.id,))
        
        connection.commit()
        connection.close()
        time.sleep(0.2)
        bot.send_message(message.from_user.id, 'Вы приобрели абонемент на ' + str(comam) + ' сессий')
        time.sleep(0.2)
    else:
        bot.send_message(message.from_user.id, 'У вас не хватает Дублонов')
































 
        
