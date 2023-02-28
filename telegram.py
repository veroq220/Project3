import telebot
from telebot import types
import sqlite3

token = "6128100453:AAHLfarNDxvw-4mpd3yy1CuNNtEPbjt1vEU"

bot = telebot.TeleBot(token)

deposit = 0

conn = sqlite3.connect('db/database.db', check_same_thread=False)
cursor = conn.cursor()


def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT INTO LifeChange (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)', (user_id, user_name, user_surname, username))
    conn.commit()


@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton('FAQ')
    button_2 = types.KeyboardButton('Pay')
    button_3 = types.KeyboardButton('Balance')
    button_4 = types.KeyboardButton('Support')
    markup.add(button_2, button_1)
    markup.add(button_3, button_4)
    bot.send_message(message.chat.id, 'Выберите нужный пункт', reply_markup=markup)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.InlineKeyboardButton(text='Продолжить', callback_data='/button')
    markup.add(button_1)
    bot.send_message(message.chat.id, 'Приветствуем в нашем Телеграмм боте для получения доступа к приватному сообществу Hardliner Industries.', reply_markup=markup)

    us_id = message.from_user.id
    us_name = message.from_user.first_name
    us_sname = message.from_user.last_name
    username = message.from_user.username

    db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == 'Продолжить':
        button_message(message)

    if message.text == 'Начало <--':
        button_message(message)

    if message.text == 'FAQ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = types.KeyboardButton('Пополнение баланса')
        button_2 = types.KeyboardButton('Об игре')
        button_3 = types.KeyboardButton('Начало <--')
        button_4 = types.KeyboardButton('Что даёт "Приватный доступ в Beta"?')
        markup.add(button_1, button_2)
        markup.add(button_4)
        markup.add(button_3)

        bot.send_message(message.chat.id, 'Какой у вас вопрос?', reply_markup=markup)

    if message.text == 'Что даёт "Приватный доступ в Beta"?':
        bot.send_message(message.chat.id, 'Вы получаете эксклюзивный доступ к ранней стадии игры Genopets с полным спектром возможностей, таких как прокачкой своего питомца, обменом шагов на энергию, заработку токена Ki и многое другое.')

    if message.text == 'Об игре':
        bot.send_message(message.chat.id, 'Фаундерами проекта являются всем известные Animoca Brands, создавшие большинство AAA проектов в криптоиндустрии.\n\nGenopets стал популярен после запуска квеста с Кристаллами, где абсолютно каждый мог решить несложные задачки и получить свой заветный кристалл.\n\nАдминистрация смогла выстроить надёжную экономическую модель с бесконечным вливом нативного токена Ki и без его применения.\nКак и ожидалось токен начал бурный двух-дневный рост, после которого последовала небольшая полугодовая коррекция.')
    elif message.text == 'Пополнение баланса':
        bot.send_message(message.chat.id, 'Чтобы пополнить баланс вам нужно: \n1. Перейти во вкладку Balance\n2. Нажать кнопку Пополнить\n3. Выбрать подходящий метод пополнения\n4. Произвести оплату и ожидать поступления средств')

    if message.text == 'Support':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = types.KeyboardButton('Telegram')
        button_2 = types.KeyboardButton('VK')
        button_3 = types.KeyboardButton('Discord')
        button_4 = types.KeyboardButton('Начало <--')
        markup.add(button_1, button_2)
        markup.add(button_3, button_4)

        bot.send_message(message.chat.id, 'Свяжитесь с нами в любой социальной сети и мы оперативно не поможем вам', reply_markup=markup)

    if message.text == 'Telegram':
        bot.send_message(message.chat.id, 'Оператор поддержки в Telegram: t.me/veroq')

    if message.text == 'VK':
        bot.send_message(message.chat.id, 'Оператор поддержки в VK: vk.com/arti_pant')

    if message.text == 'Discord':
        bot.send_message(message.chat.id, 'Наш Discord, помощь в канале Dota2: https://discord.gg/xeKhjh53')

    if message.text == 'Balance':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = types.KeyboardButton('Пополнить')
        button_2 = types.KeyboardButton('Вывести')
        button_3 = types.KeyboardButton('Мой Баланс')
        button_4 = types.KeyboardButton('Начало <--')
        markup.add(button_1, button_2)
        markup.add(button_3, button_4)

        bot.send_message(message.chat.id, 'Какая операция вам требуется?', reply_markup=markup)

    if message.text == 'Пополнить':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = types.KeyboardButton('TRC-20')
        button_2 = types.KeyboardButton('BSC')
        button_3 = types.KeyboardButton('Polygon')
        button_4 = types.KeyboardButton('Начало <--')
        markup.add(button_1, button_2)
        markup.add(button_3, button_4)

        bot.send_message(message.chat.id, 'Выберите удобный способ пополнения', reply_markup=markup)

    if message.text == 'TRC-20':
        new_deposit = 0
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_4 = types.KeyboardButton('Начало <--')
        markup.add(button_4)

    if message.text == 'Вывести':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_4 = types.KeyboardButton('Начало <--')
        markup.add(button_4)
        bot.send_message(message.chat.id, 'Захотел)', reply_markup=markup)


bot.polling(none_stop=True, interval=0)
