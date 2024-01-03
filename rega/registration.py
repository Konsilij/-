import telebot
import sqlite3
import time



registrationnotwo = False




tsibdreg = 10
vinosbdreg = 5
manabdreg = 1
silabdreg = 14
moneybdreg = 30
dhkbdreg = 3
donatbdreg = 0
tokennsbdreg = 0
photos = 1


#Переменные для Dostups in bd BaseDostups

teachingbdreg = 1
world1bdreg = 0
world2bdreg = 0
world3bdreg = 0
klanbdreg = 0
sectbdreg = 0
raidbdreg = 0
abonements = 5
fighting = 0
narush = 0

proriv01bdreg = 1
proriv12bdreg = 1
proriv23bdreg = 1
proriv34bdreg = 1
proriv45bdreg = 1
proriv56bdreg = 1
proriv67bdreg = 1
proriv78bdreg = 1
proriv89bdreg = 1
proriv910bdreg = 1
ten_slabbdreg = 1
slab_normbdreg = 1
norm_istbdreg = 1



rang0bdreg = 0
rang1bdreg = 1
rang2bdreg = 1
rang3bdreg = 1
rang4bdreg = 1
rang5bdreg = 1
rang6bdreg = 1
rang7bdreg = 1
rang8bdreg = 1
rang9bdreg = 1
rang10bdreg = 1
rangslabbogbdreg = 1
rangnormbogbdreg = 1
rangistbogbdreg = 1



def reg_in_gorod(message):
    global registrationnotwo

    if registrationnotwo == False:



        #Первичная таблица
        global tsibdreg
        global vinosbdreg
        global manabdreg
        global silabdreg
        global moneybdreg
        global dhkbdreg
        global donatbdreg
        global tokennsbdreg
        global photos

        #Таблица для доступов
        global teachingbdreg
        global world1bdreg
        global world2bdreg
        global world3bdreg
        global klanbdreg
        global sectbdreg
        global raidbdreg
        global abonements
        global fighting
        global narush
        
        #Таблица для прорывов
        global proriv01bdreg
        global proriv12bdreg
        global proriv23bdreg
        global proriv34bdreg
        global proriv45bdreg
        global proriv56bdreg
        global proriv67bdreg
        global proriv78bdreg
        global proriv89bdreg
        global proriv910bdreg
        global ten_slabbdreg
        global slab_normbdreg
        global norm_istbdreg 



        #Таблица для рангов
        global rang0bdreg
        global rang1bdreg
        global rang2bdreg
        global rang3bdreg
        global rang4bdreg
        global rang5bdreg
        global rang6bdreg
        global rang7bdreg
        global rang8bdreg
        global rang9bdreg
        global rang10bdreg
        global rangslabbogbdreg
        global rangnormbogbdreg
        global rangistbogbdreg


        
        # Проверяем, есть ли пользователь в базе данных
        connection = sqlite3.connect('BaseUsersy.db')
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM Users WHERE telegram_id = ?', (message.chat.id,))
        user = cursor.fetchone()
        connection.commit()
        connection.close()



        connection = sqlite3.connect('BaseUsersy.db')
        cursor = connection.cursor()

        cursor.execute('SELECT referal_id FROM Users WHERE telegram_id = ?', (message.chat.id,))
        refer = cursor.fetchone()
        connection.commit()
        connection.close()
        #if refer is NONE:
        #Тут тоже нужно кое-что сделать


        if user is None:
            ref_id = get_ref_id(message.text) # получаем идентификатор реферера
            if ref_id: # если он есть
                ifrefyes(message)
                bot.send_message(message.chat.id, f"Вы перешли по реферальной ссылке от пользователя с ID {ref_id}")
            else:
                ifrefno(message)# если его нет
                bot.send_message(message.chat.id, "Вы запустили бота без реферальной ссылки")
            time.sleep(1.0)
#hfgkjfdhgjhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
        
            
            print("Регистрацию начал " + str(message.chat.id))
            #Добавление уникального игрового айди
            bot.send_message(message.chat.id, 'Внимание! Сейчас начнется процесс регистрации. Ничего не пишите и не присылайте боту, иначе вы застрянете, и бот не сможет с вами связаться.\nО успешном завершении регистрации бот вас уведомит.')
            time.sleep(3.0)
            connection = sqlite3.connect('BaseUsersy.db')
            cursor = connection.cursor()
            cursor.execute('SELECT MAX(id) FROM Users')
            new_id = cursor.fetchone()
            ide = new_id[0]
            plus_user_id = ide + 1

            
            bot.send_message(message.chat.id, 'Идет присвоение айди, ожидайте...')
            connection.commit()
            connection.close()
            time.sleep(3.5)

#Рефералка

            
                
            #Создание записей в таблице Users, бд Usersy

#Регистрация для криминала
            connection = sqlite3.connect('BaseUsersy.db')
            cursor = connection.cursor()

            cursor.execute('''
                INSERT INTO DpULSvobodi (chat_id, LH, LM, BK, PodpolBoi)
                VALUES (?, ?, ?, ?, ?)
            ''', (message.chat.id, 0, 0, 0, 0))
            
            bot.send_message(message.chat.id, 'Связи со свободой установлены.')
            time.sleep(1.5)
            connection.commit()
            connection.close()
            


            #Создание записей в таблице Dostups, бд Usersy

            connection = sqlite3.connect('BaseUsersy.db')
            cursor = connection.cursor()

            cursor.execute('''
                INSERT INTO Dostups (telegram_id_for_dostups, teahing, world1, world2, world3, klan, sect, raid, abonems, fighting, narush)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (message.chat.id, teachingbdreg, world1bdreg, world2bdreg, world3bdreg, klanbdreg, sectbdreg, raidbdreg, abonements, fighting, narush))
            
            bot.send_message(message.chat.id, 'Все допуски выданы, ожидайте завершения регистрации...')
            time.sleep(1.5)
            connection.commit()
            connection.close()
            time.sleep(3.0)


            #Создание записей в таблице Prorivs, бд Proriv

            
            connection = sqlite3.connect('BaseUsersy.db')
            cursor = connection.cursor()

            cursor.execute('''
                INSERT INTO Prorivs (telegram_id_for_prorivs, proriv01, proriv12, proriv23, proriv34, proriv45, proriv56, proriv67, proriv78, proriv89, proriv910, ten_slab, slab_norm, norm_ist)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (message.chat.id, proriv01bdreg, proriv12bdreg, proriv23bdreg, proriv34bdreg, proriv45bdreg, proriv56bdreg, proriv67bdreg, proriv78bdreg, proriv89bdreg, proriv910bdreg, ten_slabbdreg, slab_normbdreg, norm_istbdreg))
            
            bot.send_message(message.chat.id, 'Ранги обозначены...')
            time.sleep(1.5)
            connection.commit()
            connection.close()
            time.sleep(2.0)

           #Создание записей в таблице Rangi, бд Ranges
            time.sleep(0.1)
            connection = sqlite3.connect('BaseUsersy.db')
            cursor = connection.cursor()

            cursor.execute('''
                INSERT INTO Rangi (telegram_id_for_rangi, rang0, rang1, rang2, rang3, rang4, rang5, rang6, rang7, rang8, rang9, rang10, rangslabbog, rangnormbog, rangistbog)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (message.chat.id, rang0bdreg, rang1bdreg, rang2bdreg, rang3bdreg, rang4bdreg, rang5bdreg, rang6bdreg, rang7bdreg, rang8bdreg, rang9bdreg, rang10bdreg, rangslabbogbdreg, rangnormbogbdreg, rangistbogbdreg))
            time.sleep(1.5)
            
            bot.send_message(message.chat.id, 'Отлично! Регистрация завершена!')
            connection.commit()
            connection.close()
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btnstart = types.KeyboardButton('Начать игру!')
            markup.add(btnstart)
            bot.send_message(message.from_user.id, 'Выделен игровой сервер номер 7. Удачной игры!', reply_markup=markup)
            print("Зарегестрирован пользователь " + str(message.chat.username))





    

        else:
            bot.send_message(message.chat.id, 'Вы уже зарегистрированы!')




    else:
            bot.send_message(message.from_user.id, 'Видимо, вы уже зарегестрированы')










