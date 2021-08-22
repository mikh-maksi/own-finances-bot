# Импортируем нужные библиотеки
from telegram.ext import Updater, MessageHandler, Filters

# пишем функцию, которая отправляет пользователю полученное сообщение (эхо-функцию)
def echo(update, context):
    update.message.reply_text(update.message.text)

# Подключаемся к боту
updater = Updater("1369610345:AAHq-1NZ7ytIj08OfUTBmToedNPoh_AHiIA")

# Определяем "Диспетчер" - объект к которому мы будем подключать обработчики
dispatcher = updater.dispatcher

# Подключение обработчика, при отправке всех сообщений запускает функцию echo
dispatcher.add_handler(MessageHandler(Filters.all, echo))

# Запускает бота
updater.start_polling()
# Когда нажимаем CTRL+C (Windows) Shift+Command+C (Mac) останавливает работу бота
updater.idle()