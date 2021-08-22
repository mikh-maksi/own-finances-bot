# Создание телеграм бота
**Телеграмм-бот** - это компьютерная программа, для месенджера Telegram. Боты позволяют автоматизировать многие действия: от предоставления информации до учета финансов и организации продаж.  
Для написания нашего телеграмм-бота мы используем язык программирования **Python** и библиотеку **python-telegram-bot**. Потому что **Python** можно запустить и локально и на сервере, а **python-telegram-bot** - это простая и обновляемая библиотека для написания телеграм-ботов.  
Телеграмм-бот - это программа, которая получает сообщения от телеграмм-пользователя, обрабатывает их и отправляет ответ.

## Среда запуска
Для того, чтобы запустить любую программу необходима среда для ее запуска. Для запуска Python нам необходимо установить интерпретатор на ваш компьютер (<a href = 'https://www.python.org/downloads/'>https://www.python.org/downloads/</a>), установить программу для работы с кодом <a href = 'https://code.visualstudio.com/download'>MS VS Code</a> и установить в ней плагин для работы с Python.



## Пустой бот
Самый простой бот - это бот, который ничего не делает. Он просто запускается. Такой бот позволит нам проверить, все ли у нас хорошо с подключением к боту и его запуском в редакторе кода.
```python
from telegram.ext import Updater

updater = Updater("1369610345:AAHq-1NZ7ytIj08OfUTBmToedNPoh_AHiIA")
dispatcher = updater.dispatcher
print("Bot is live!")

updater.start_polling()
updater.idle()
```

## Эхо-бот
Самым простым функционалом для телеграм-бота является эхо-бот. Эхо-бот - это такой бот, который отправляет в ответ все сообщения, которые он получил. Ниже приведен код бота, который отправляет в ответ тот же текст сообщения, который получает от пользователя.

```python
from telegram.ext import Updater, MessageHandler, Filters

def echo(update, context):
    update.message.reply_text(update.message.text)

updater = Updater("1369610345:AAHq-1NZ7ytIj08OfUTBmToedNPoh_AHiIA")
dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(Filters.all, echo))

updater.start_polling()
updater.idle()
```