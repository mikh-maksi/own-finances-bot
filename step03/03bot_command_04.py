from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

def echo(update, context):
    string_in = update.message.text
    if string_in =='/start':
        update.message.reply_text("Hello! This is bot!")
    if string_in =='/help':
        update.message.reply_text("This is help for you!")


updater = Updater("1958845613:AAF48B3sKwrn-ggwr8LxGdYiygpyePLBs9I")
dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(Filters.all, echo))

updater.start_polling()
updater.idle()
