
#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
Basic example for a bot that uses inline keyboards. For an in-depth explanation, check out
 https://git.io/JOmFw.
"""
import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [InlineKeyboardButton("Анализ", callback_data='11'),InlineKeyboardButton("Стратегия", callback_data='22'),InlineKeyboardButton("Продукты И процессы", callback_data='33'),InlineKeyboardButton("Ресурсы", callback_data='44'),InlineKeyboardButton("ИНдикация", callback_data='55'),],
        [InlineKeyboardButton("Не понятно", callback_data='8')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Выберите сферу:', reply_markup=reply_markup)


def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    keyboard_16p = [[InlineKeyboardButton("Не понятно", callback_data='1'),InlineKeyboardButton("Не продумано", callback_data='2'),InlineKeyboardButton("Не прописано", callback_data='3'),InlineKeyboardButton("Не внедрен фреймворк", callback_data='4'),InlineKeyboardButton("Не автоматизировано", callback_data='5')],]

    reply_markup_16p = InlineKeyboardMarkup(keyboard_16p)



    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    print(query.data)

    if query.data == '11':
        query.edit_message_text(text=f"Оцените уровень детализации решений в сфере анализа", reply_markup=reply_markup_16p)
    elif query.data == '22':
        query.edit_message_text(text=f"Оцените уровень детализации решений в сфере стратегии", reply_markup=reply_markup_16p)
    elif query.data == '33':
        query.edit_message_text(text=f"Оцените уровень детализации решений в сфере Продуктов и процессов", reply_markup=reply_markup_16p)
    elif query.data == '44':
        query.edit_message_text(text=f"Оцените уровень детализации решений в сфере Ресурсов", reply_markup=reply_markup_16p)
    elif query.data == '55':
        query.edit_message_text(text=f"Оцените уровень детализации решений в сфере иНдикации", reply_markup=reply_markup_16p)

    else:
        query.edit_message_text(text=f"Ссылка на оплату")

def help_command(update: Update, context: CallbackContext) -> None:
    """Displays info on how to use the bot."""
    update.message.reply_text("Use /start to test this bot.")


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("")

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
