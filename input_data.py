from telegram.ext import Updater, MessageHandler, Filters

def echo(update, context):
    string_in = update.message.text
    elements = string_in.split(' ')

    if elements[0]=='/create_event':
        name = elements[1]
        place = elements[2]
        time = elements[3]
        print(name,place,time)
        f = open('event_list.txt','a')
        string_out_f = f'{name} {place} {time}';
        f.write(string_out_f+'\n')

        f.close()

    if elements[0]=='/show_events':
        f = open('event_list.txt','r')
        string = ''
        for line in f:
            string += line
        chat = update.effective_chat
        context.bot.send_message(chat_id=chat.id, text=string)
updater = Updater("2014714331:AAG5HQXZIaf_XyC2dx8OiUfp8WbtBdZNgGk")

dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(Filters.all, echo))

updater.start_polling()
updater.idle()
        
