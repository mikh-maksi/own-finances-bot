from telegram.ext import Updater, CommandHandler


def start(update, context):
	chat = update.effective_chat
	context.bot.send_message(chat_id=chat.id, text="Hello! This is own finances bot.")

updater = Updater("")

dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))


updater.start_polling()
updater.idle()