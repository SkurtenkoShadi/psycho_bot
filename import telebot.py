import telebot
import pyodbc
import datetime
import datetime
from datetime import date
from telebot import types
db = pyodbc.connect(driver='{SQL Server}',
                      server='SHADI\msqlserver',
                      database='register',
                      user='user',
                      password='sa')
bot = telebot.TeleBot('6740853015:AAGHkAjxNfdhi15uA1y0o8_8yP7ynVhgnDE')
print(db)
@bot.message_handler(commands=["start"])
def start(message):
    global newuserflag
    newuserflag = 0
    chat_id = message.chat.id
    first_name = message.chat.first_name
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    k1 = types.KeyboardButton(text= "Взаимоотношения с родителями")
    k2 = types.KeyboardButton(text="Взаимоотношения с детьми")
    k3 = types.KeyboardButton(text="Взаимоотношения с партнёром")
    markup.add(k1).row (k2, k3)
    bot.send_message(chat_id, f"Здравствуйте, {first_name}! Я Добби, семейный бот-психолог, у меня вы можете пройти первичную диагностику, записаться на консультацию или приобрести обучающую программу. Какая тема вас интересует?", reply_markup=markup)
    bot.register_next_step_handler(message, vzaim)
def vzaim(message):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     global pass_id
     pass_id = message.text
     chat_id = message.chat.id
     
     if pass_id == "Взаимоотношения с родителями":
        k1 = types.KeyboardButton(text= "Гнев")
        k2 = types.KeyboardButton(text="Печаль")
        k3 = types.KeyboardButton(text="Тревога")
        k4 = types.KeyboardButton(text= "Страх")
        k5 = types.KeyboardButton(text="Вина")
        k6 = types.KeyboardButton(text="Стыд")
        k7 = types.KeyboardButton(text= "Отвращение")
        k8 = types.KeyboardButton(text="Я не знаю")
        markup.add(k1, k2, k3, k4, k5, k6, k7, k8)
        bot.send_message(chat_id, "Какие эмоции вы испытываете при общении с родителями?", reply_markup=markup)
     elif pass_id == "Взаимоотношения с детьми":
            k1 = types.KeyboardButton(text= "Гнев")
            k2 = types.KeyboardButton(text="Печаль")
            k3 = types.KeyboardButton(text="Тревога")
            k4 = types.KeyboardButton(text= "Страх")
            k5 = types.KeyboardButton(text="Вина")
            k6 = types.KeyboardButton(text="Стыд")
            k7 = types.KeyboardButton(text= "Отвращение")
            k8 = types.KeyboardButton(text="Я не знаю")
            bot.send_message(chat_id, "Какие эмоции вы испытываете при общении с детьми?", reply_markup=markup)
            markup.add(k1, k2, k3, k4, k5, k6, k7, k8)
     elif pass_id == "Взаимоотношения с партнером":
            k1 = types.KeyboardButton(text= "Гнев")
            k2 = types.KeyboardButton(text="Печаль")
            k3 = types.KeyboardButton(text="Тревога")
            k4 = types.KeyboardButton(text= "Страх")
            k5 = types.KeyboardButton(text="Вина")
            k6 = types.KeyboardButton(text="Стыд")
            k7 = types.KeyboardButton(text= "Отвращение")
            k8 = types.KeyboardButton(text="Я не знаю")
            markup.add(k1, k2, k3, k4, k5, k6, k7, k8)
            bot.send_message(chat_id, "Какие эмоции вы испытываете при общении с партнером?", reply_markup=markup)
     bot.register_next_step_handler(message, mark)
def mark(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(chat_id, "Как вы оцениваете вашу коммуникацию с родителями от 1-10? Введите число.", reply_markup=markup)
    bot.register_next_step_handler(message, problem)
def problem(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if pass_id == "Взаимоотношения с родителями":   
        k1 = types.KeyboardButton(text= "Гиперопека")
        k2 = types.KeyboardButton(text="Тирания")
        k3 = types.KeyboardButton(text="Отсутствие вовлеченности")
        k4 = types.KeyboardButton(text="Конфликт поколений")
        markup.add(k1, k2, k3, k4)
        bot.send_message(chat_id, "Какая проблема затрагивает ваши отношения с родителями больше всего?", reply_markup=markup)
    elif pass_id == "Взаимоотношения с детьми":   
        k1 = types.KeyboardButton(text= "Соперничество между детьми")
        k2 = types.KeyboardButton(text="Зависимость от гаджетов")
        k3 = types.KeyboardButton(text="Эмоциональная нестабильность")
        k4 = types.KeyboardButton(text="Неавторитетность родителя")
        markup.add(k1, k2, k3, k4)
        bot.send_message(chat_id, "Какая проблема затрагивает ваши отношения с детьми больше всего?", reply_markup=markup)
    elif pass_id == "Взаимоотношения с партнером":   
        k1 = types.KeyboardButton(text= "Абьюз")
        k2 = types.KeyboardButton(text="Тирания")
        k3 = types.KeyboardButton(text="Пресыщение или отвержение")
        k4 = types.KeyboardButton(text="Конфликт интересов")
        markup.add(k1, k2, k3, k4) 
        bot.send_message(chat_id, "Какая проблема затрагивает ваши отношения с партнёром больше всего?", reply_markup=markup)
    bot.register_next_step_handler(message, kurs)
def kurs (message):
    global gl_mess
    gl_mess = message.text
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    k1 = types.KeyboardButton(text= "Курс")
    k2 = types.KeyboardButton(text="Консультация")
    markup.add(k1, k2) 
    bot.send_message(chat_id, "Я проанализировал ваши ответы и могу предложить вам записаться на наш курс или личную консультацию. Что вам подходит?", reply_markup=markup)
    bot.register_next_step_handler(message, choise)
def choise(message):
    chat_id = message.chat.id
    global write
    write = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if write == "Курс":
        if pass_id == "Взаимоотношения с родителями":
            bot.send_message(chat_id,f"Вы записаны на курс: {pass_id}.\nСпасибо за доверие", reply_markup=markup)
        elif pass_id == "Взаимоотношения с детьми":
            bot.send_message(chat_id,f"Вы записаны на курс: {pass_id}.\nСпасибо за доверие", reply_markup=markup)
        elif pass_id == "Взаимоотношения с детьми":
            bot.send_message(chat_id,f"Вы записаны на курс: {pass_id}.\nСпасибо за доверие ", reply_markup=markup)
    elif write == "Консультация":
        current_date = date.today()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        cursor = db.cursor()
        count = 0
        for i in range(7):
            incr = current_date + datetime.timedelta(days=i+1)
            cursor.execute(f"SELECT reg_date FROM reg WHERE reg_date ='{incr}' AND reg_flag = 0")
            newdate = cursor.fetchone()
            if newdate is None:
                continue
            else:
                finaldate = newdate[0]
                markup.add(types.KeyboardButton(text = f"{finaldate}"))
                count = count+1
        if count == 0:
            bot.send_message(chat_id, "К сожалению, в ближайшую неделю нет свободных записей", reply_markup = markup)
            bot.register_next_step_handler(message, choise)
        else:
            bot.send_message(chat_id, "Выберите удобный для вас день:", reply_markup = markup)
            bot.register_next_step_handler(message, time_choise)
def time_choise(message):
    global c_date
    c_date = message.text
    cursor = db.cursor()
    cursor.execute(f"SELECT reg_time FROM reg WHERE reg_date = '{c_date}' AND reg_flag	= 0")
    time = cursor.fetchall()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if time is None:
        bot.send_message(message.chat.id, "К сожалению, на эту дату нет свободных записей", reply_markup = markup)
        bot.register_next_step_handler(message, choise)
    else:           
        for x in time:
            x = x[0]
            markup.add(types.KeyboardButton(text =f"{x}"))
        bot.send_message(message.chat.id, "Пожалуйста, выберите удобное для вас время", reply_markup = markup)
        bot.register_next_step_handler(message, time_reg)
def time_reg(message):
    c_time = message.text
    cursor = db.cursor()
    cursor.execute(f"UPDATE reg SET reg_flag = 1 WHERE reg_date = '{c_date}' AND reg_time = '{c_time}'")
    cursor.commit()      
    bot.send_message(message.chat.id, "Вы успешно записались на консультацию", reply_markup=types.ReplyKeyboardRemove())
bot.polling(none_stop=True, interval=0)