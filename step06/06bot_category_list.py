from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

def start(update, context):
    categ_list = ['eat','ent','coffee','transport', 'sport', 'clothers','other']
    string_out = ' '.join(categ_list)
    f = open('categ_list.txt','w')
    f.write(string_out)
    f.close()

    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Hello! This home finance bot.")


def cat(update, context):
    f = open('categ_list.txt','r')
    for line in f:
        string = line
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text=string)
    

def costs(update, context):

    string = update.message.text
    elements = string.split(' ')
    
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Your cost is "+elements[1])


def echo(update, context):
    update.message.reply_text(update.message.text)

updater = Updater("1958845613:AAF48B3sKwrn-ggwr8LxGdYiygpyePLBs9I")
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("eat", costs))
dispatcher.add_handler(CommandHandler("cat", cat))
dispatcher.add_handler(MessageHandler(Filters.all, echo))

updater.start_polling()
updater.idle()