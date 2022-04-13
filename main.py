import logging
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = '5284222325:AAHt4CqmR3tPcFwGz5vjDnilQ2xxpnRrg-U'


def start(update, context):
    update.message.reply_text(
        "Привет! Я эхо-бот. Напишите мне что-нибудь, и я пришлю это назад!")


def first(update, context):
    update.message.reply_text('Создатель, функция создана успешно!')


def help(update, context):
    update.message.reply_text(
        "Я бот справочник.")


def echo(update, context):
    an = update.message.text
    if 'пошел' in an:
        an = 'Ну и иди!'
    update.message.reply_text(an)


def main():
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    text_handler = MessageHandler(Filters.text, echo)

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("first", first))
    dp.add_handler(text_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
