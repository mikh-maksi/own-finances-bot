from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

n_costs = 0 

def start(update, context):
    f = open('categories.txt', 'w')
    f.write('eat ent coffee transport sport clothers other')
    f.close()
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Hello! This home finance bot.")

def costs(update, context):
    global n_costs

    string = update.message.text
    costs = string.split(' ')
    n_costs = n_costs + int(costs[1])
    
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Your costs is "+str(n_costs))
    # f = open('/Users/mac/Documents/work/python/own-finances-bot/python-telegram-bot/log_bot.txt', 'w')
    f = open('log_bot.txt', 'a')
    f.write(update.message.text)
    f.write(' \n')
    f.close()

def total(update, context):
    f =  open('log_bot.txt', 'r')
    n_total=0
    for line in f:
        elements = line.split(' ')
        n_total = n_total +int(elements[1])       
    f.close()
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Your costs is "+str(n_total))

def cat(update, context):
    f =  open('categories.txt', 'r')
    for line in f:
        elements = line.split(' ')
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text=line)


def addcat(update, context):
    f =  open('categories.txt', 'r')
    for line in f:
        categories = line.split(' ') #категории
    f.close()
    string = update.message.text
    commands = string.split(' ')
    chat = update.effective_chat

    if commands[1] in categories:
        context.bot.send_message(chat_id=chat.id, text="Категория "+commands[1]+" уже существует!")
    else:
        f =  open('categories.txt', 'w')
        for el in categories:
            f.write(el+' ')
        f.write(commands[1])
        f.close()
        context.bot.send_message(chat_id=chat.id, text="Категория "+commands[1]+" добавлена!")


def echo(update, context):
    update.message.reply_text(update.message.text)

updater = Updater("1369610345:AAHq-1NZ7ytIj08OfUTBmToedNPoh_AHiIA")
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("costs", costs))
dispatcher.add_handler(CommandHandler("total", total))
dispatcher.add_handler(CommandHandler("addcat", addcat))
dispatcher.add_handler(CommandHandler("cat", cat))
dispatcher.add_handler(MessageHandler(Filters.all, echo))

updater.start_polling()
updater.idle()