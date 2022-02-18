# Own finances bot

## Step01
Эхо-бот.

```python
from telegram.ext import Updater, MessageHandler, Filters

def echo(update, context):
    print(update.message.text)
    update.message.reply_text(update.message.text)

updater = Updater("")
dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(Filters.all, echo))

updater.start_polling()
updater.idle()


```

## Step02
Команда `/start`
```python
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

def echo(update, context):
    string_in = update.message.text
    if string_in =='/start':
        update.message.reply_text("Hello! This is bot!")


updater = Updater("1958845613:AAF48B3sKwrn-ggwr8LxGdYiygpyePLBs9I")
dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(Filters.all, echo))

updater.start_polling()
updater.idle()
```

```python
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

def start(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Hello! This is own finances bot.")

def echo(update, context):
    update.message.reply_text(update.message.text)

updater = Updater("")
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.all, echo))

updater.start_polling()
updater.idle()

```


## Step03
```python
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

def start(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Hello! This is own finances bot.")

def costs(update, context):

    string = update.message.text
    elements = string.split(' ')
    
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Your cost is "+elements[1])


def echo(update, context):
    update.message.reply_text(update.message.text)

updater = Updater("")
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("costs", costs))
dispatcher.add_handler(MessageHandler(Filters.all, echo))

updater.start_polling()
updater.idle()

```

## Step04
Категории списком
```python
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler


categ_list = ['eat','ent','coffee','transport', 'sport', 'clothers','other']
cost = 0
def start(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Hello! This home finance bot.")


def category(update, context):
    string = ''
    for line in categ_list:
        string += ' '+line
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text=string)


def costs(update, context):
    global cost
    string = update.message.text
    elements = string.split(' ')
    cost += int(elements[1])
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Your cost is "+str(cost))


def echo(update, context):
    update.message.reply_text(update.message.text)

updater = Updater("1958845613:AAF48B3sKwrn-ggwr8LxGdYiygpyePLBs9I")
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler(categ_list, costs))
dispatcher.add_handler(CommandHandler("category", category))
dispatcher.add_handler(MessageHandler(Filters.all, echo))

updater.start_polling()
updater.idle()

```

## Step05
Чтение списка категорий из файла
```python
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

```

## Step06
Сохраняем значение затрат в файл


```python
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import os

def cat_list_value():
    if os.path.exists("categ_list.txt"):
        f = open('categ_list.txt','r')
        for line in f:
            string = line
        elements = string.split(' ')
        f.close()
        return elements
    else:
        return []



def start(update, context):
    categ_list = ['eat','ent','coffee','transport', 'sport', 'clothers','other']
    string_out = ' '.join(categ_list)
    f = open('categ_list.txt','w')
    f.write(string_out)
    f.close()
    
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Hello! This is own finances bot.")

def cat (update, context):
    f = open('categ_list.txt','r')
    for line in f:
        string = line
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text=string)

def addcat (update, context): #/addcat tech
    string = update.message.text
    elements = string.split(' ')
    f = open('categ_list.txt','r')
    for line in f:
        categories = line
    f.close
    f = open('categ_list.txt','w')
    f.write(categories)
    f.write(' '+elements[1])
    f.close()
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Category "+elements[1]+" added.")


def costs(update, context):

    string = update.message.text
    elements = string.split(' ')
    
    f = open('costs_list.txt','a')
    f.write(string+'\n')
    f.close()

    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Your cost is "+elements[1])

def echo(update, context):
    update.message.reply_text(update.message.text)

updater = Updater("1958845613:AAF48B3sKwrn-ggwr8LxGdYiygpyePLBs9I")
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler(cat_list_value(), costs))
dispatcher.add_handler(CommandHandler("cat", cat))
dispatcher.add_handler(CommandHandler("addcat", addcat))

dispatcher.add_handler(MessageHandler(Filters.all, echo))

updater.start_polling()
updater.idle()

```

## Step07
Значение по категориям

```python
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import os

def cat_list_value():
    if os.path.exists("categ_list.txt"):
        f = open('categ_list.txt','r')
        for line in f:
            string = line
        elements = string.split(' ')
        f.close()
        return elements
    else:
        return []

def total(update, context):
    total_dict = dict.fromkeys(cat_list_value(),0)

    fin_list = []
    f = open('costs_list.txt','r')
    for line in f:
        elements = line.split(' ')
        lst = [elements[0][1:],int(elements[1])]
        fin_list.append(lst)

    for lst in fin_list:
        total_dict[lst[0]] = total_dict[lst[0]] + lst[1]

    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text=str(total_dict))


def costs_list(update, context):
    f = open('costs_list.txt','r')
    string = ''
    for line in f:
        string = string + line
    f.close()
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text=string)

def start(update, context):
    categ_list = ['eat','ent','coffee','transport', 'sport', 'clothers','other']
    string_out = ' '.join(categ_list)
    f = open('categ_list.txt','w')
    f.write(string_out)
    f.close()
    
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Hello! This is own finances bot.")

def cat (update, context):
    f = open('categ_list.txt','r')
    for line in f:
        string = line
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text=string)

def addcat (update, context): #/addcat tech
    string = update.message.text
    elements = string.split(' ')
    f = open('categ_list.txt','r')
    for line in f:
        categories = line
    f.close
    f = open('categ_list.txt','w')
    f.write(categories)
    f.write(' '+elements[1])
    f.close()
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Category "+elements[1]+" added.")


def costs(update, context):

    string = update.message.text
    elements = string.split(' ')
    
    f = open('costs_list.txt','a')
    f.write(string+'\n')
    f.close()

    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Your cost is "+elements[1])

def echo(update, context):
    update.message.reply_text(update.message.text)

updater = Updater("1958845613:AAF48B3sKwrn-ggwr8LxGdYiygpyePLBs9I")
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler(cat_list_value(), costs))
dispatcher.add_handler(CommandHandler("cat", cat))
dispatcher.add_handler(CommandHandler("addcat", addcat))
dispatcher.add_handler(CommandHandler("costs", costs_list))
dispatcher.add_handler(CommandHandler("total", total))


dispatcher.add_handler(MessageHandler(Filters.all, echo))

updater.start_polling()
updater.idle()

```

## Step08
Использование функции
```python


```

## Step09

Кнопки 1
```python


```

## Step10
Кнопки 2
```python


```

??? Учет ID отправителя