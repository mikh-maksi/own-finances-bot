from telegram.ext import Updater, MessageHandler, Filters

def echo(update, context):
    string = update.message.text
    print(string[0])
    if  '/' in string[0] : 
        chat = update.effective_chat
        context.bot.send_message(chat_id=chat.id, text="This is command")
    update.message.reply_text(update.message.text)

updater = Updater("1369610345:AAHq-1NZ7ytIj08OfUTBmToedNPoh_AHiIA")
dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(Filters.all, echo))

updater.start_polling()
updater.idle()