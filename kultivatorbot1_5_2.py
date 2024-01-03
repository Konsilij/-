import sqlite3
import time
import telebot
from telebot import types



bot = telebot.TeleBot('6970053055:AAGp8_DivHfDSkckYW3o7qicvCz7ihbji74')

#Технические переменные

hnya = 23
Nepovtorka = False




rarest = True
radingst = False
status = False











nowstate = rarest




#Переменные для игры









#Вычисления переменных






#Перевалочные переменные




































































#Показывает статус игрока

@bot.message_handler(commands=['statusmykt'])
def handle_status(message):
    global hnya
    
    bot.send_message(message.from_user.id, 'Кольцо-колечко, скажи кто я, кольцо-колечко, скажи что есть у меня.')
    connection = sqlite3.connect('BaseUsersy.db')
    cursor = connection.cursor()
    cursor.execute('SELECT tsi FROM Users WHERE chat_id = ?',(message.chat.id,))
    usertsi = cursor.fetchone()
    connection.commit()
    connection.close()

    connection = sqlite3.connect('BaseUsersy.db')
    cursor = connection.cursor()
    cursor.execute('SELECT vinos FROM Users WHERE chat_id = ?',(message.chat.id,))
    uservinos = cursor.fetchone()
    connection.commit()
    connection.close()

    connection = sqlite3.connect('BaseUsersy.db')
    cursor = connection.cursor()
    cursor.execute('SELECT mana FROM Users WHERE chat_id = ?',(message.chat.id,))
    usermana = cursor.fetchone()
    connection.commit()
    connection.close()



    connection = sqlite3.connect('BaseUsersy.db')
    cursor = connection.cursor()
    cursor.execute('SELECT sila FROM Users WHERE chat_id = ?',(message.chat.id,))
    usersila = cursor.fetchone()
    connection.commit()
    connection.close()



    connection = sqlite3.connect('BaseUsersy.db')
    cursor = connection.cursor()
    cursor.execute('SELECT money FROM Users WHERE chat_id = ?',(message.chat.id,))
    usermoney = cursor.fetchone()
    connection.commit()
    connection.close()

    connection = sqlite3.connect('BaseUsersy.db')
    cursor = connection.cursor()
    cursor.execute('SELECT duh_kris FROM Users WHERE chat_id = ?',(message.chat.id,))
    userduh_kris = cursor.fetchone()
    connection.commit()
    connection.close()

    connection = sqlite3.connect('BaseUsersy.db')
    cursor = connection.cursor()
    cursor.execute('SELECT donat FROM Users WHERE chat_id = ?',(message.chat.id,))
    userdonat = cursor.fetchone()
    connection.commit()
    connection.close()

    connection = sqlite3.connect('BaseUsersy.db')
    cursor = connection.cursor()
    cursor.execute('SELECT tokenns FROM Users WHERE chat_id = ?',(message.chat.id,))
    usertokenns = cursor.fetchone()
    connection.commit()
    connection.close()


    connection = sqlite3.connect('BaseUsersy.db')
    cursor = connection.cursor()
    cursor.execute('SELECT klan FROM Dostups WHERE telegram_id_for_dostups = ?',(message.chat.id,))
    klantrorfalse = cursor.fetchone()
    connection.commit()
    connection.close()

    
    
    bot.send_message(message.from_user.id, f'Клан: {klantrorfalse}')
        







    connection = sqlite3.connect('BaseUsersy.db')
    cursor = connection.cursor()
    # Получение списка столбцов из таблицы
    cursor.execute('PRAGMA table_info(Rangi)')
    columns = [column[1] for column in cursor.fetchall()]

# Поиск столбца с значением 0
    for column in columns:
        query = f'SELECT {column} FROM Rangi WHERE telegram_id_for_rangi = ? AND {column} = 0'
        cursor.execute(query, (message.chat.id,))
        result = cursor.fetchone()
    
        if result is not None:
            bot.send_message(message.from_user.id, f'Ваш ранг {column}')
            # Найден столбец, выводим его название
            
            
        else:
            hnya += 1
        







    
    if usertsi is not None:
        if uservinos is not None:
            if usermana is not None:
                if usersila is not None:
                    if usermoney is not None:
                        if userduh_kris is not None:
                            if userdonat is not None:
                                if usertokenns is not None:
                                    bot.send_message(message.from_user.id, f'Вот ваши истинные данные:\n' + 'Единиц Ци: ' + str(usertsi[0]) + '\n' + 'Выносливость: ' + str(uservinos[0]) + '\nМана: ' + str(usermana[0]) + '\nСила: ' + str(usersila[0]) + '\nКоличество Дублонов: ' + str(usermoney[0]) + '\nКоличество нейтральных духовных кристаллов: ' + str(userduh_kris[0]) + '\nАлмазов: ' + str(userdonat[0]) + '\nМонет Удачи: ' + str(uservinos[0]))
                                    



                                else:
                                    print("error with usertokenns")
                            else:
                                print("error with userdonat")
                        else:
                            print("error with userkris_duh")
                    else:
                        print("error with usermoney")
                else:
                    print("error with usersila")
            else:
                print("error with usermana")
        else:
            print("error with uservinos")
    else:
        print("error with usertsi ")
    

    
    

































#Тут идет типа регистрация. Переменные для таблицы Users in bd Usersy

tsibdreg = 10
vinosbdreg = 5
manabdreg = 1
silabdreg = 14
moneybdreg = 30
dhkbdreg = 3
donatbdreg = 0
tokennsbdreg = 0



#Переменные для Dostups in bd BaseDostups

teachingbdreg = 1
world1bdreg = 0
world2bdreg = 0
world3bdreg = 0
klanbdreg = 0
sectbdreg = 0
raidbdreg = 0


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











@bot.message_handler(commands=['reg', 'registration'])
def handle_start(message):
    #Первичная таблица
    global tsibdreg
    global vinosbdreg
    global manabdreg
    global silabdreg
    global moneybdreg
    global dhkbdreg
    global donatbdreg
    global tokennsbdreg


    #Таблица для доступов
    global teachingbdreg
    global world1bdreg
    global world2bdreg
    global world3bdreg
    global klanbdreg
    global sectbdreg
    global raidbdreg



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
    if user is None:
        #Добавление уникального игрового айди
        bot.send_message(message.chat.id, 'Внимание! Сейчас начнется процесс регистрации. Ничего не пишите и не присылайте боту, иначе вы застрянете, и бот не сможет с вами связаться.\nО успешном завершении регистрации бот вас уведомит.')
        time.sleep(3.0)
        connection = sqlite3.connect('BaseUsersy.db')
        cursor = connection.cursor()
        cursor.execute('SELECT MAX(id) FROM Users')
        maks_id_tuple = cursor.fetchone()
        if maks_id_tuple is not None and maks_id_tuple[0] is not None:
            maks_id = maks_id_tuple[0]
        else:
            maks_id = 0
        plus_user_id = maks_id + 1

        
        bot.send_message(message.chat.id, 'Идет присвоение айди, ожидайте...')
        connection.commit()
        connection.close()
        time.sleep(3.5)




        #Создание записей в таблице Users, бд Usersy
        user_name = message.chat.username if message.chat.username else 'default_username'
        connection = sqlite3.connect('BaseUsersy.db')
        cursor = connection.cursor()

        cursor.execute('''
            INSERT INTO Users (id, chat_id, telegram_id, user_name, tsi, vinos, mana, sila, money, duh_kris, donat, tokenns)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (plus_user_id, message.chat.id, message.chat.id, user_name, tsibdreg, vinosbdreg, manabdreg, silabdreg, moneybdreg, dhkbdreg, donatbdreg, tokennsbdreg))
        connection.commit()
        bot.send_message(message.chat.id, 'Создание первичной таблицы завершено, ожидайте...')
        connection.commit()
        connection.close()
        time.sleep(2.5)
        
        


        #Создание записей в таблице Dostups, бд Usersy

        connection = sqlite3.connect('BaseUsersy.db')
        cursor = connection.cursor()

        cursor.execute('''
            INSERT INTO Dostups (telegram_id_for_dostups, teahing, world1, world2, world3, klan, sect, raid)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (message.chat.id, teachingbdreg, world1bdreg, world2bdreg, world3bdreg, klanbdreg, sectbdreg, raidbdreg))
        connection.commit()
        bot.send_message(message.chat.id, 'Все допуски выданы, ожидайте завершения регистрации...')
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
        connection.commit()
        bot.send_message(message.chat.id, 'Ранги обозначены...')
        connection.commit()
        connection.close()
        time.sleep(2.0)

       #Создание записей в таблице Rangi, бд Ranges
        time.sleep(2.0)
        connection = sqlite3.connect('BaseUsersy.db')
        cursor = connection.cursor()

        cursor.execute('''
            INSERT INTO Rangi (telegram_id_for_rangi, rang0, rang1, rang2, rang3, rang4, rang5, rang6, rang7, rang8, rang9, rang10, rangslabbog, rangnormbog, rangistbog)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (message.chat.id, rang0bdreg, rang1bdreg, rang2bdreg, rang3bdreg, rang4bdreg, rang5bdreg, rang6bdreg, rang7bdreg, rang8bdreg, rang9bdreg, rang10bdreg, rangslabbogbdreg, rangnormbogbdreg, rangistbogbdreg))
        connection.commit()
        bot.send_message(message.chat.id, 'Отлично! Регистрация завершена!')
        connection.commit()
        connection.close()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btnstart = types.KeyboardButton('Начать игру!')
        markup.add(btnstart)
        bot.send_message(message.from_user.id, 'Выделен игровой сервер номер 7. Удачной игры!', reply_markup=markup)






    








    else:
        bot.send_message(message.chat.id, 'Вы уже зарегистрированы!')



















#Обработчик начала сюжетки

@bot.message_handler(func=lambda message: True)
def handle_text_1(message):
    global Nepovtorka
    global hnya
    if message.text == 'Начать игру!':
        bot.send_message(message.from_user.id, 'Великий фермер, добившись всего в своем мире, выращивал божественную полынь, единственное растение, которое он еще не вырастил.')
        time.sleep(4.0)
        bot.send_message(message.from_user.id, 'Он копался в земле, когда почувствовал что его тянет вниз, куда-то под землю.')
        time.sleep(3.0)
        bot.send_message(message.from_user.id, 'Закричал, хватаясь руками за воздух, но это не помогло и он все равно падал в бездну!')
        time.sleep(3.0)
        bot.send_message(message.from_user.id, 'И в конце-концов, он упал...')
        time.sleep(7.0)
        bot.send_message(message.from_user.id, 'Где я? Я... Живой?')
        time.sleep(2.3)
        bot.send_message(message.from_user.id, 'Так Фермер и попал в другой мир. Он встретил благородного старца, который рассказал ему про мир...')
        time.sleep(7.5)
        bot.send_message(message.from_user.id, '- Это мир Обучения, и сюда попадают те, кто упал с небес.\nЭто мир Ци! Тут есть могущественные культиваторы, создания, которые используют свою ци для вознесения...')
        time.sleep(4.0)
        bot.send_message(message.from_user.id, 'Старец многое рассказал вам, и также много он дал вам.')
        time.sleep(4.0)
        bot.send_message(message.from_user.id, '- Удачи тебе, практик! И еще, запомни - будь праведным культиватором, и тогда тебя никто не тронет!\nНо ежели ты вступишь в секту, то ничем хорошим это не закончится.')
        time.sleep(4.0)
        pecherastart = open('C:/Users/Евгений/OneDrive/Рабочий стол/Культиватор/photos/pecherastart.png', 'rb')
        bot.send_photo(message.from_user.id, pecherastart)
        bot.send_message(message.from_user.id, 'Старец исчез в клубах дыма, а вы осознали что находитесь в пещере.\nРядом стоит чашка с прозрачной водой, льняной халат лежит на каменном полу пещеры, а еще там лежит кольцо.\nВы протянули к нему руки, и бронзовое кольцо наделось на ваш палец')
        time.sleep(6.0)
        bot.send_message(message.from_user.id, 'Это кольцо может показать вам, кто вы есть на самом деле, просто скажите "/statusmykt"')
        time.sleep(9.0)
        bot.send_message(message.from_user.id, 'Посмотрели? Отлично! Пора отправляться в приключения. Но перед этим стоит заглянуть в местный город, и попытаться немного заработать.\nВ небесном мире ценятся только духовные кристаллы, но и золотые монетки тоже пока сойдут.')
        time.sleep(2.0)
        
        bot.send_message(message.from_user.id, '_Если ты застрял, то нажми на "/escape" - это должно помочь. Но, к сожалению, это может нарушить баланс игры, поэтому эту функцию можно использовать лишь пять раз в день.\nЕсли что-то серьезное, пиши мне в лс._', parse_mode='Markdown')
        time.sleep(3.0)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Да, я готов.")
        btn2 = types.KeyboardButton("Нет, у меня нет времени")
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, '_Готов покорить вершины культивации и стать самым сильным?_', reply_markup=markup, parse_mode='Markdown')
    elif message.text == 'Да, я готов.':
        if Nepovtorka == False:
            Nepovtorka = True
            time.sleep(2.0)
            kras = open('C:/Users/Евгений/OneDrive/Рабочий стол/Культиватор/photos/kraspeisajgstart.jpg', 'rb')
            bot.send_photo(message.from_user.id, kras)
            bot.send_message(message.from_user.id, 'Вы выбрались из пещеры, и увидели красочные пейзажи местности...')
            time.sleep(4.0)
            bot.send_message(message.from_user.id, 'Оглядевшись по сторонам, невдалеке вы увидели небольшой городок. Подумав, вы решили отправится туда.')
            time.sleep(5.0)
            bot.send_message(message.from_user.id, '*Топаю. Топ-топ-топ, а я иду вперед!*', parse_mode='Markdown')
            time.sleep(4.0)
            bot.send_message(message.from_user.id, 'За несколько часов пути, вы наконец добрались до города. Перед вами открылся поистине великолепный вид средневекового города.')
            gorodokstart = open('C:/Users/Евгений/OneDrive/Рабочий стол/Культиватор/photos/gorodokstart.jpg', 'rb')
            bot.send_photo(message.from_user.id, gorodokstart)
            time.sleep(4.0)
            bot.send_message(message.from_user.id, 'Окинув взором этот городок, вы решили отправится на постоялый двор, а уже после пойти гулять по городу.')
            time.sleep(3.0)
            bot.send_message(message.from_user.id, 'Пройдя по узеньким улочкам, вы вышли во двор, где как раз располагалась подходящая гостинница')
            time.sleep(4.0)
            bot.send_message(message.from_user.id, '"Тут я и остановлюсь."- решили вы.')
            gostina = open('C:/Users/Евгений/OneDrive/Рабочий стол/Культиватор/photos/gostin.png', 'rb')
            bot.send_photo(message.from_user.id, gostina)
            time.sleep(4.0)
            bot.send_message(message.from_user.id, 'Вы заплатили за аренду, и у вас почти не осталось монет. Вы присели на веранду, и начали думать, что делать, и куда пойти.')
            verandas = open('C:/Users/Евгений/OneDrive/Рабочий стол/Культиватор/photos/veranda.png', 'rb')
            bot.send_photo(message.from_user.id, verandas)
            time.sleep(6.0)
            bot.send_message(message.from_user.id, '_Вот и началась твоя самостоятельная жизнь. Многие культиваторы этого мира отсекли бы себе руку только за шанс получить такие перспективы развития! Развивайся... И однажды ты повергнешь самих богов..._', parse_mode='Markdown')
            time.sleep(6.0)
            bot.send_message(message.from_user.id, '_С окружающим миром разберешся сам, или просто заплатишь за информацию. Ах да, за жизнь, аренду, да и вообще за все нужно платить, поэтому, как можно быстрее пойди в рейд, или просто выполни задание, которое есть на доске объявлений_', parse_mode='Markdown')
            time.sleep(3.0)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Переход к главному меню")
            markup.add(btn1)
            bot.send_message(message.from_user.id, ':)', reply_markup=markup)
        else:
            hnya += 1






    




        















@bot.message_handler(func=lambda message: True)
def handle_text_2(message):
    if message.text == 'Переход к главному меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Город")
        btn2 = types.KeyboardButton("Канцелярия")
        btn3 = types.KeyboardButton("Гостинница")
        btn4 = types.KeyboardButton("Клановая область")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, ':)', reply_markup=markup)



























if __name__ == '__main__':
    bot.polling(none_stop=True)


