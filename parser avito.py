import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# Ваш токен бота
TOKEN = '5181195595:AAEjtfkldOSlfzu2miVKDmetgXLFznEQ8j0'

# Объект бота
bot = telegram.Bot(token=TOKEN)

# Объект для обновления бота
updater = Updater(token=TOKEN)

# Обработчик команды /start
def start(update, context):
    # Создаем клавиатуру с двумя кнопками
    keyboard = [[InlineKeyboardButton("Запустить", callback_data='start'),
                 InlineKeyboardButton("Выйти", callback_data='exit')]]

    # Создаем разметку клавиатуры
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем сообщение пользователю с клавиатурой
    update.message.reply_text('Выберите действие:', reply_markup=reply_markup)

# Обработчик нажатия на кнопки
def button(update, context):
    query = update.callback_query

    if query.data == 'start':
        query.answer()
        query.edit_message_text(text="Запускаем бота...")

    elif query.data == 'exit':
        query.answer()
        query.edit_message_text(text="До свидания!")

# Добавляем обработчики команд и нажатий на кнопки
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(button))

# Запускаем бота
updater.start_polling()

# Останавливаем бота при нажатии Ctrl+C
updater.idle()

