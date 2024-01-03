import sqlite3
import time
import telebot
from telebot import types
import logging
from settings import phtsetings

# Технические переменные

hnya = 23
Nepovtorka = False
Nepovtorka_for_start_game = False
registrationnotwo = False

rarest = True
radingst = False
status = False

nowstate = rarest


# Переменные для игры


# Вычисления переменных


# Перевалочные переменные


# Показывает статус игрока
def handle_status(message):
    global hnya

    message.send_message(message.from_user.id, 'Кольцо-колечко, скажи кто я, кольцо-колечко, скажи что есть у меня.')
    connection = sqlite3.connect('BaseUsersy.db')
    cursor = connection.cursor()
    cursor.execute('SELECT tsi FROM Users WHERE chat_id = ?', (message.chat.id,))
    usertsi = cursor.fetchone()
    connection.commit()
    connection.close()

    connection = sqlite3.connect('BaseUsersy.db')
    cursor = connection.cursor()
    cursor.execute('SELECT vinos FROM Users WHERE chat_id = ?', (message.chat.id,))
    uservinos = cursor.fetchone()
    connection.commit()
    connection.close()

    connection = sqlite3.connect('BaseUsersy.db')
    cursor = connection.cursor()
    cursor.execute('SELECT mana FROM Users WHERE chat_id = ?', (message.chat.id,))
    usermana = cursor.fetchone()
    connection.commit()
    connection.close()

    connection = sqlite3.connect('BaseUsersy.db')
    cursor = connection.cursor()
    cursor.execute('SELECT sila FROM Users WHERE chat_id = ?', (message.chat.id,))
    usersila = cursor.fetchone()
    connection.commit()
    connection.close()

    connection = sqlite3.connect('BaseUsersy.db')
    cursor = connection.cursor()
    cursor.execute('SELECT money FROM Users WHERE chat_id = ?', (message.chat.id,))
    usermoney = cursor.fetchone()
    connection.commit()
    connection.close()

    connection = sqlite3.connect('BaseUsersy.db')
    cursor = connection.cursor()
    cursor.execute('SELECT duh_kris FROM Users WHERE chat_id = ?', (message.chat.id,))
    userduh_kris = cursor.fetchone()
    connection.commit()
    connection.close()

    connection = sqlite3.connect('BaseUsersy.db')
    cursor = connection.cursor()
    cursor.execute('SELECT donat FROM Users WHERE chat_id = ?', (message.chat.id,))
    userdonat = cursor.fetchone()
    connection.commit()
    connection.close()

    connection = sqlite3.connect('BaseUsersy.db')
    cursor = connection.cursor()
    cursor.execute('SELECT tokenns FROM Users WHERE chat_id = ?', (message.chat.id,))
    usertokenns = cursor.fetchone()
    connection.commit()
    connection.close()

    connection = sqlite3.connect('BaseUsersy.db')
    cursor = connection.cursor()
    cursor.execute('SELECT klan FROM Dostups WHERE telegram_id_for_dostups = ?', (message.chat.id,))
    klantrorfalse = cursor.fetchone()
    connection.commit()
    connection.close()

    message.send_message(message.from_user.id, f'Клан: {klantrorfalse}')

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
            message.send_message(message.from_user.id, f'Ваш ранг {column}')
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
                                    message.send_message(message.from_user.id,
                                                         f'Вот ваши истинные данные:\n' + 'Единиц Ци: ' + str(
                                                             usertsi[0]) + '\n' + 'Выносливость: ' + str(
                                                             uservinos[0]) + '\nМана: ' + str(
                                                             usermana[0]) + '\nСила: ' + str(
                                                             usersila[0]) + '\nКоличество Дублонов: ' + str(usermoney[
                                                                                                                0]) + '\nКоличество нейтральных духовных кристаллов: ' + str(
                                                             userduh_kris[0]) + '\nАлмазов: ' + str(
                                                             userdonat[0]) + '\nМонет Удачи: ' + str(uservinos[0]))




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


# Тут идет типа регистрация. Переменные для таблицы Users in bd Usersy

tsibdreg = 10
vinosbdreg = 5
manabdreg = 1
silabdreg = 14
moneybdreg = 30
dhkbdreg = 3
donatbdreg = 0
tokennsbdreg = 0
photos = 1

# Переменные для Dostups in bd BaseDostups

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


def ref(message):
    ref_link = f"https://t.me/{message.get_me().username}?start={message.from_user.id}"  # генерируем реферальную ссылку с ID пользователя
    message.send_message(message.chat.id, f"Ваша реферальная ссылка: {ref_link}")  # отправляем ее пользователю


def get_ref_id(text):
    return text.split()[1] if len(text.split()) > 1 else None


def ifrefyes(message):
    ref_id = get_ref_id(message.text)
    nagrada_after(message)

    # nhjconnection

    connection = sqlite3.connect('BaseUsersy.db')
    cursor = connection.cursor()

    message.send_message(ref_id,
                         'По вашей реферальной ссылке зарегестрировался новый реферал. Дублоны поступили в кольцо. Поздравляем!')

    message.send_message(message.chat.id, 'Награждаем реферала и его проводника...')

    user_name = message.chat.username if message.chat.username else 'default_username'

    cursor.execute('''
        INSERT INTO Users (id, chat_id, telegram_id, user_name, tsi, vinos, mana, sila, money, duh_kris, donat, tokenns, photos, polkarma, nopolkarma, referal_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (message.chat.id, message.chat.id, message.chat.id, user_name, tsibdreg, vinosbdreg, manabdreg, silabdreg,
          moneybdreg, dhkbdreg, donatbdreg, tokennsbdreg, photos, 0, 0, ref_id))

    message.send_message(message.chat.id, 'Создание первичной таблицы завершено, ожидайте...')
    time.sleep(1.5)
    connection.commit()
    connection.close()


def ifrefno(message):
    ref_idno = None
    user_name = message.chat.username if message.chat.username else 'default_username'

    connection = sqlite3.connect('BaseUsersy.db')
    cursor = connection.cursor()

    #

    cursor.execute('''
        INSERT INTO Users (id, chat_id, telegram_id, user_name, tsi, vinos, mana, sila, money, duh_kris, donat, tokenns, photos, polkarma, nopolkarma, referal_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (message.chat.id, message.chat.id, message.chat.id, user_name, tsibdreg, vinosbdreg, manabdreg, silabdreg,
          moneybdreg, dhkbdreg, donatbdreg, tokennsbdreg, photos, 0, 0, ref_idno))

    message.send_message(message.chat.id, 'Создание первичной таблицы завершено, ожидайте...')
    time.sleep(1.5)
    connection.commit()
    connection.close()


def banningstart(message):
    usersg_name = message.chat.username if message.chat.username else 'ВАМИ'
    connection = sqlite3.connect('BaseUsersy.db')
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO Dostups (telegram_id_for_dostups, teahing, world1, world2, world3, klan, sect, raid, abonems, fighting, narush)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (message.chat.id, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1))
    time.sleep(1.5)
    message.send_message(message.chat.id, f'ВАШ АККАУНТ АВТОМАТИЧЕСКИ ЗАБАНЕН ЗА НЕСОБЛЮДЕНИИ {usersg_name} ПРАВИЛ')

    connection.commit()
    connection.close()


stop = False
kllicenc = False
licencpodp = False


def license_text(name):
    return f'__ВНИМАНИЕ!\nВВОДЯ "Принимаю условия" ВЫ АВТОМАТИЧЕСКИ СОГЛАШАЕТЕСЬ СО ВСЕМИ УСЛОВИЯМИ СОГЛАШЕНИЯ МЕЖДУ @kultivatorbot И @{name} (ИГРОКОМ).\nВ СЛУЧАЕ НЕВЫПОЛНЕНИЯ ОБЯЗАТЕЛЬСТВ ИГРОКОМ(ВАМИ), АДМИНИСТРАЦИЯ ИМЕЕТ ОТОЗВАТЬ ЛИЦЕНЗИЮ НА ИСПОЛЬЗОВАНИЕ БОТА В РАЗВЛЕКАТЕЛЬНЫХ И ЛЮБЫХ ДРУГИХ ЦЕЛЯХ.\nЛИЦЕНЗИЯ, ОБЯЗАТЕЛЬСТВА И ПРАВА ДОСТУПНЫ ПО НАЖАТИЮ "Условия".'


# лИЦЕНЗИЯ

def vib(message):
    usersg_name = message.chat.username if message.chat.username else 'ВАМИ'
    kb = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton("Принимаю условия")
    btn2 = types.KeyboardButton("Не принимаю условия")
    kb.add(btn1, btn2)
    text = license_text(usersg_name)

    # message.send_message(chat_id=message.chat.id, text=text)
    print(text)


def nodf(message):
    rd = message.text.split()[1] if len(message.text.split()) > 1 else None
    return rd


# Тут кроется ошибка с рефералкой
def ch_n_ref(message):
    ref_id = nodf(message)
    if ref_id is not None:
        nagrada_after(ref_id)
    else:
        pass
    return ref_id


def ifingstart(message):
    connection = sqlite3.connect('BaseUsersy.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Users WHERE telegram_id = ?', (message.chat.id,))
    usersd = cursor.fetchone()
    connection.commit()
    connection.close()
    usersg_name = message.chat.username if message.chat.username else 'ВАМИ'

    if usersd is None:
        vib(message)
        ref_id = ch_n_ref(message)
    else:
        message.send_message(message.chat.id,
                             'Возможно, вы уже зарегестрированы. Если это не так, обратитесь в администрацию')


def licenceyesorno(message):
    global licencpodp
    global kllicenc

    connection = sqlite3.connect('BaseUsersy.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Users WHERE telegram_id = ?', (message.chat.id,))
    usersb = cursor.fetchone()
    connection.commit()
    connection.close()
    if usersb is None:
        if message.text == 'Принимаю условия':

            licencpodp = True
            print("come")

            handle_reg(message)
        elif message.text == 'Не принимаю условия':
            kllicenc = True
            banningstart(message)
            message.send_message(message.chat.id, 'ВНИМАНИЕ! АВТОМАТИЧЕСКАЯ БЛОКИРОВКА АККАУНТА.')
    else:
        message.send_message(message.chat.id, 'Возможно, вы уже зарегестрированы')


def llyes():
    global licencpodp

    licencpodp = True
    handle_reg(message)


def llno():
    global kllicenc
    kllicenc = True

    banningstart(message)


def handle_reg(message):
    chatik = message.chat.id
    global registrationnotwo
    chat_info = message.get_chat(message.chat.id)
    if message.chat:
        chat_id = message.chat.id
        print(f"Chat ID: {chat_id}")

    else:
        print("Chat information not available.")
    if registrationnotwo == False:

        # Первичная таблица
        global tsibdreg
        global vinosbdreg
        global manabdreg
        global silabdreg
        global moneybdreg
        global dhkbdreg
        global donatbdreg
        global tokennsbdreg
        global photos

        # Таблица для доступов
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

        # Таблица для прорывов
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

        # Таблица для рангов
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
        # if refer is NONE:

        # Тут тоже нужно кое-что сделать

        if user is None:
            ref_id = get_ref_id(message.text)  # получаем идентификатор реферера
            if ref_id:  # если он есть
                ifrefyes(message)
                message.send_message(message.chat.id, f"Вы перешли по реферальной ссылке от пользователя с ID {ref_id}")
            else:
                ifrefno(message)  # если его нет
                message.send_message(message.chat.id, "Вы запустили бота без реферальной ссылки")
            time.sleep(1.0)
            # hfgkjfdhgjhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh

            print("Регистрацию начал " + str(message.chat.id))
            # Добавление уникального игрового айди

            message.send_message(message.chat.id,
                                 'Внимание! Сейчас начнется процесс регистрации. Ничего не пишите и не присылайте боту, иначе вы застрянете, и бот не сможет с вами связаться.\nО успешном завершении регистрации бот вас уведомит.')
            time.sleep(3.0)
            connection = sqlite3.connect('BaseUsersy.db')
            cursor = connection.cursor()
            cursor.execute('SELECT MAX(id) FROM Users')
            new_id = cursor.fetchone()
            ide = new_id[0]
            plus_user_id = ide + 1

            message.send_message(message.chat.id, 'Идет присвоение айди, ожидайте...')
            connection.commit()
            connection.close()
            time.sleep(3.5)

            # Рефералка

            # Создание записей в таблице Users, бд Usersy

            # Регистрация для криминала
            connection = sqlite3.connect('BaseUsersy.db')
            cursor = connection.cursor()

            cursor.execute('''
            INSERT INTO DpULSvobodi (chat_id, LH, LM, BK, PodpolBoi)
            VALUES (?, ?, ?, ?, ?)
        ''', (message.chat.id, 0, 0, 0, 0))

            message.send_message(message.chat.id, 'Связи со свободой установлены.')
            time.sleep(1.5)
            connection.commit()
            connection.close()

            # Создание записей в таблице Dostups, бд Usersy

            connection = sqlite3.connect('BaseUsersy.db')
            cursor = connection.cursor()

            cursor.execute('''
            INSERT INTO Dostups (telegram_id_for_dostups, teahing, world1, world2, world3, klan, sect, raid, abonems, fighting, narush)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
                message.chat.id, teachingbdreg, world1bdreg, world2bdreg, world3bdreg, klanbdreg, sectbdreg,
                raidbdreg,
                abonements, fighting, narush))

            message.send_message(message.chat.id, 'Все допуски выданы, ожидайте завершения регистрации...')
            time.sleep(1.5)
            connection.commit()
            connection.close()
            time.sleep(3.0)

            # Создание записей в таблице Prorivs, бд Proriv

            connection = sqlite3.connect('BaseUsersy.db')
            cursor = connection.cursor()

            cursor.execute('''
            INSERT INTO Prorivs (telegram_id_for_prorivs, proriv01, proriv12, proriv23, proriv34, proriv45, proriv56, proriv67, proriv78, proriv89, proriv910, ten_slab, slab_norm, norm_ist)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
                message.chat.id, proriv01bdreg, proriv12bdreg, proriv23bdreg, proriv34bdreg, proriv45bdreg,
                proriv56bdreg,
                proriv67bdreg, proriv78bdreg, proriv89bdreg, proriv910bdreg, ten_slabbdreg, slab_normbdreg,
                norm_istbdreg))

            message.send_message(message.chat.id, 'Ранги обозначены...')
            time.sleep(1.5)
            connection.commit()
            connection.close()
            time.sleep(2.0)

            # Создание записей в таблице Rangi, бд Ranges
            time.sleep(0.1)
            connection = sqlite3.connect('BaseUsersy.db')
            cursor = connection.cursor()

            cursor.execute('''
            INSERT INTO Rangi (telegram_id_for_rangi, rang0, rang1, rang2, rang3, rang4, rang5, rang6, rang7, rang8, rang9, rang10, rangslabbog, rangnormbog, rangistbog)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (message.chat.id, rang0bdreg, rang1bdreg, rang2bdreg, rang3bdreg, rang4bdreg, rang5bdreg, rang6bdreg,
              rang7bdreg, rang8bdreg, rang9bdreg, rang10bdreg, rangslabbogbdreg, rangnormbogbdreg, rangistbogbdreg))
            time.sleep(1.5)

            message.send_message(message.chat.id, 'Отлично! Регистрация завершена!')
            connection.commit()
            connection.close()
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btnstart = types.KeyboardButton('Начать игру!')
            markup.add(btnstart)
            message.send_message(message.from_user.id, 'Выделен игровой сервер номер 7. Удачной игры!',
                                 reply_markup=markup)
            print("Зарегестрирован пользователь " + str(message.chat.username))







        else:
            message.send_message(message.chat.id, 'Вы уже зарегистрированы!')




    else:
        message.send_message(message.from_user.id, 'Видимо, вы уже зарегестрированы')


# Обработчик начала сюжетки

def handle_text_1(message):
    global Nepovtorka
    global hnya
    global Nepovtorka_for_start_game
    if message.text == 'Начать игру!':
        if Nepovtorka_for_start_game == False:
            message.send_message(message.from_user.id,
                                 'Великий фермер, добившись всего в своем мире, выращивал божественную полынь, единственное растение, которое он еще не вырастил.')
            time.sleep(4.0)
            message.send_message(message.from_user.id,
                                 'Он копался в земле, когда почувствовал что его тянет вниз, куда-то под землю.')
            time.sleep(3.0)
            message.send_message(message.from_user.id,
                                 'Закричал, хватаясь руками за воздух, но это не помогло и он все равно падал в бездну!')
            time.sleep(3.0)
            message.send_message(message.from_user.id, 'И в конце-концов, он упал...')
            time.sleep(7.0)
            message.send_message(message.from_user.id, 'Где я? Я... Живой?')
            time.sleep(2.3)
            message.send_message(message.from_user.id,
                                 'Так Фермер и попал в другой мир. Он встретил благородного старца, который рассказал ему про мир...')
            time.sleep(7.5)
            message.send_message(message.from_user.id,
                                 '- Это мир Обучения, и сюда попадают те, кто упал с небес.\nЭто мир Ци! Тут есть могущественные культиваторы, создания, которые используют свою ци для вознесения...')
            time.sleep(4.0)
            message.send_message(message.from_user.id, 'Старец многое рассказал вам, и также много он дал вам.')
            time.sleep(4.0)
            message.send_message(message.from_user.id,
                                 '- Удачи тебе, практик! И еще, запомни - будь праведным культиватором, и тогда тебя никто не тронет!\nНо ежели ты вступишь в секту, то ничем хорошим это не закончится.')
            time.sleep(4.0)
            pecherastart = open('C:/Users/Евгений/OneDrive/Рабочий стол/Культиватор/photos/pecherastart.png', 'rb')
            message.send_photo(message.from_user.id, pecherastart)
            message.send_message(message.from_user.id,
                                 'Старец исчез в клубах дыма, а вы осознали что находитесь в пещере.\nРядом стоит чашка с прозрачной водой, льняной халат лежит на каменном полу пещеры, а еще там лежит кольцо.\nВы протянули к нему руки, и бронзовое кольцо наделось на ваш палец')
            time.sleep(6.0)
            message.send_message(message.from_user.id,
                                 'Это кольцо может показать вам, кто вы есть на самом деле, просто скажите "/statusmykt"')
            time.sleep(9.0)
            message.send_message(message.from_user.id,
                                 'Посмотрели? Отлично! Пора отправляться в приключения. Но перед этим стоит заглянуть в местный город, и попытаться немного заработать.\nВ небесном мире ценятся только духовные кристаллы, но и золотые монетки тоже пока сойдут.')
            time.sleep(2.0)

            message.send_message(message.from_user.id,
                                 '_Если ты застрял, то нажми на "/escape" - это должно помочь. Но, к сожалению, это может нарушить баланс игры, поэтому эту функцию можно использовать лишь пять раз в день.\nЕсли что-то серьезное, пиши мне в лс._',
                                 parse_mode='Markdown')
            time.sleep(3.0)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Да, я готов.")
            btn2 = types.KeyboardButton("Нет, у меня нет времени")
            markup.add(btn1, btn2)
            message.send_message(message.from_user.id, '_Готов покорить вершины культивации и стать самым сильным?_',
                                 reply_markup=markup, parse_mode='Markdown')
        else:
            hnya += 1
    elif message.text == 'Да, я готов.':
        if Nepovtorka == False:
            Nepovtorka = True
            time.sleep(2.0)
            kras = open('C:/Users/Евгений/OneDrive/Рабочий стол/Культиватор/photos/kraspeisajgstart.jpg', 'rb')
            message.send_photo(message.from_user.id, kras)
            message.send_message(message.from_user.id,
                                 'Вы выбрались из пещеры, и увидели красочные пейзажи местности...')
            time.sleep(4.0)
            message.send_message(message.from_user.id,
                                 'Оглядевшись по сторонам, невдалеке вы увидели небольшой городок. Подумав, вы решили отправится туда.')
            time.sleep(5.0)
            message.send_message(message.from_user.id, '*Топаю. Топ-топ-топ, а я иду вперед!*', parse_mode='Markdown')
            time.sleep(4.0)
            message.send_message(message.from_user.id,
                                 'За несколько часов пути, вы наконец добрались до города. Перед вами открылся поистине великолепный вид средневекового города.')
            gorodokstart = open('C:/Users/Евгений/OneDrive/Рабочий стол/Культиватор/photos/gorodokstart.jpg', 'rb')
            message.send_photo(message.from_user.id, gorodokstart)
            time.sleep(4.0)
            message.send_message(message.from_user.id,
                                 'Окинув взором этот городок, вы решили отправится на постоялый двор, а уже после пойти гулять по городу.')
            time.sleep(3.0)
            message.send_message(message.from_user.id,
                                 'Пройдя по узеньким улочкам, вы вышли во двор, где как раз располагалась подходящая гостинница')
            time.sleep(4.0)
            message.send_message(message.from_user.id, '"Тут я и остановлюсь."- решили вы.')
            gostina = open('C:/Users/Евгений/OneDrive/Рабочий стол/Культиватор/photos/gostin.png', 'rb')
            message.send_photo(message.from_user.id, gostina)
            time.sleep(4.0)
            message.send_message(message.from_user.id,
                                 'Вы заплатили за аренду, и у вас почти не осталось монет. Вы присели на веранду, и начали думать, что делать, и куда пойти.')
            verandas = open('C:/Users/Евгений/OneDrive/Рабочий стол/Культиватор/photos/veranda.png', 'rb')
            message.send_photo(message.from_user.id, verandas)
            time.sleep(6.0)
            message.send_message(message.from_user.id,
                                 '_Вот и началась твоя самостоятельная жизнь. Многие культиваторы этого мира отсекли бы себе руку только за шанс получить такие перспективы развития! Развивайся... И однажды ты повергнешь самих богов..._',
                                 parse_mode='Markdown')
            time.sleep(6.0)
            message.send_message(message.from_user.id,
                                 '_С окружающим миром разберешся сам, или просто заплатишь за информацию. Ах да, за жизнь, аренду, да и вообще за все нужно платить, поэтому, как можно быстрее пойди в рейд, или просто выполни задание, которое есть на доске объявлений_',
                                 parse_mode='Markdown')
            time.sleep(3.0)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Переход к главному меню")
            markup.add(btn1)
            message.send_message(message.from_user.id, ':)', reply_markup=markup)
        else:
            hnya += 1


def handle_menuh(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Городок")
    btn2 = types.KeyboardButton("Канцелярия")
    btn3 = types.KeyboardButton("Гостинница")
    btn4 = types.KeyboardButton("Клановая область")
    markup.add(btn1, btn2, btn3, btn4)
    message.send_message(message.from_user.id, '(:', reply_markup=markup)


def nagrada_after(message):
    refd_id = ch_n_ref(message)
    if refd_id is not None:
        connection = sqlite3.connect('BaseUsersy.db')
        cursor = connection.cursor()
        # Тут нужно добавить награду ********************************************************************************************************************************
        cursor.execute('SELECT money FROM Users WHERE chat_id = ?', (refd_id,))
        time.sleep(1.0)

        plusmonforref = cursor.fetchone()

    elif refd_id is None:
        message.send_message(message.chat.id, 'Неверный код реферала')
        refd_id = None

    elif plusmonforref == None:
        if refd_id is not None:
            message.send_message(message.chat.id, 'Пусто')
        else:
            message.send_message(message.chat.id, 'Данного реферала не существует')
    else:
        pass
    pf = plusmonforref[0]
    time.sleep(0.2)
    connection.commit()
    connection.close()

    if plusmonforref != None:

        pfnow = pf + 25

        connection = sqlite3.connect('BaseUsersy.db')
        cursor = connection.cursor()

        cursor.execute('UPDATE Users SET money = ? WHERE chat_id = ?', (pfnow, ref_id,))
        time.sleep(1.0)

        connection.commit()
        connection.close()

    else:
        pass
