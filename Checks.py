from telegram.ext import Updater, MessageHandler, Filters

def echo(update, context):
    string_in = update.message.text
    elements = string_in.split(' ')
    string_out = ''
    categories = ['eat','transport','ent']
    print(elements)

    command=elements[0]
    value = elements[1]
    command_name = command[1:]
    print(command_name)

    if command_name in categories:
        string_out += 'Cost category is in the list\n'
    else:
        string_out += 'Cost category is not in the list\n'

    if string_in[0] == '/':
        string_out += 'This is command\n'
    else:
        string_out += 'This is text\n'

    if value.isdigit():
        string_out += 'Value is digit\n'
    else:
        string_out += 'Value is not digit\n'



    if string_in == '/start':
        string_out += 'Hello! This is new bot!\n New bot.'

    if string_in == '/help':
        string_out += 'Avaliable commands\n/start - meet message \n/t1 /t2 /t3 /t4 - texts in bot'

    if string_in == '/t1':
        string_out += 'Text1'

    if string_in == '/t2':
        string_out = 'Text1'

    if string_in == '/t3':
        string_out = 'Text1'

    if string_in == '/t4':
        string_out = 'Text1'


    update.message.reply_text(string_out)

updater = Updater("2014714331:AAG5HQXZIaf_XyC2dx8OiUfp8WbtBdZNgGk")

dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(Filters.all, echo))

updater.start_polling()
updater.idle()
