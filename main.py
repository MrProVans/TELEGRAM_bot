import logging
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = '5284222325:AAHt4CqmR3tPcFwGz5vjDnilQ2xxpnRrg-U'


def start(update, context):
    reply_keyboard = [['/address', '/phone'],
                      ['/site', '/work_time']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    update.message.reply_text(
        "Я бот-справочник. Какая информация вам нужна?",
        reply_markup=markup
    )


def close_keyboard(update, context):
    update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


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


def address(update, context):
    update.message.reply_text(
        "Адрес: г. Москва, ул. Льва Толстого, 16")


def phone(update, context):
    update.message.reply_text("Телефон: +7(495)776-3030")


def site(update, context):
    update.message.reply_text(
        "Сайт: http://www.yandex.ru/company")


def work_time(update, context):
    update.message.reply_text(
        "Время работы: круглосуточно.")


def main():
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    text_handler = MessageHandler(Filters.text, echo)

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("close", close_keyboard))
    dp.add_handler(CommandHandler("first", first))
    dp.add_handler(CommandHandler("Адрес", address))
    dp.add_handler(CommandHandler("phone", phone))
    dp.add_handler(CommandHandler("site", site))
    dp.add_handler(CommandHandler("work_time", work_time))
    dp.add_handler(text_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
