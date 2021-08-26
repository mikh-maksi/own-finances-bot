from telegram.ext import Updater

updater = Updater("1369610345:AAHq-1NZ7ytIj08OfUTBmToedNPoh_AHiIA")
dispatcher = updater.dispatcher

updater.start_polling()
updater.idle()