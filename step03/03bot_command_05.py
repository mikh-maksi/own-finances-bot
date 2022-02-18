from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

def echo(update, context):
    string_in = update.message.text
    if string_in =='/start':
        update.message.reply_text("Hello! This is bot!")
    if string_in =='/help':
        update.message.reply_text("This is help for you!")
    if string_in =='/commands':
        update.message.reply_text("/q1 /q2 /q3")
    if string_in =='/q1':
        update.message.reply_text("Answer for question 1")
    if string_in =='/q2':
        update.message.reply_text("Answer for question 2")
    if string_in =='/q3':
        update.message.reply_text("Answer for question 3")


updater = Updater("1958845613:AAF48B3sKwrn-ggwr8LxGdYiygpyePLBs9I")
dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(Filters.all, echo))

updater.start_polling()
updater.idle()
