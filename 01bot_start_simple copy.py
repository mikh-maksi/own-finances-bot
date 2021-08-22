from telegram.ext import Updater, CommandHandler


def start(update, context):
	chat = update.effective_chat
	context.bot.send_message(chat_id=chat.id, text="Привет, я Финансовый бот")


updater = Updater("1369610345:AAHq-1NZ7ytIj08OfUTBmToedNPoh_AHiIA")

dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))

# Запускает бота
updater.start_polling()
# Когда нажимаем CTRL+C (Windows) Shift+Command+C (Mac) останавливает работу бота
updater.idle()