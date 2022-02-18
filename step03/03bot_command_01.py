from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

def echo(update, context):
    if update.message.text.isdigit():
        update.message.reply_text("is digit")
    else:
        update.message.reply_text("is not digit")


updater = Updater("1958845613:AAF48B3sKwrn-ggwr8LxGdYiygpyePLBs9I")
dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(Filters.all, echo))

updater.start_polling()
updater.idle()
