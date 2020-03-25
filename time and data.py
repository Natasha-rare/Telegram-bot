# Импортируем необходимые классы.
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
import time


def help(update, context):
    update.message.reply_text(
        "Я пока не умею помогать... Я только ваше эхо.")


def time_1(update, context):
    t = ' '.join(str(time.asctime()).split()[1:3]) + str(str(time.asctime()).split()[-1])
    update.message.reply_text(t)

def date(update, context):
    update.message.reply_text(str(time.asctime()).split()[-2])

def start(update, context):
    update.message.reply_text(
        "Привет! Я эхо-бот. Напишите мне что-нибудь, и я пришлю это назад!")


def main():

    updater = Updater(TOKEN, use_context=True)
    # Создаём объект updater.
    # Вместо слова "TOKEN" надо разместить полученный от @BotFather токен

    # Получаем из него диспетчер сообщений.
    dp = updater.dispatcher

    # Создаём обработчик сообщений типа Filters.text
    # из описанной выше функции echo()
    # После регистрации обработчика в диспетчере
    # эта функция будет вызываться при получении сообщения
    # с типом "текст", т. е. текстовых сообщений.

    # Регистрируем обработчик в диспетчере.
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler('time', time_1))
    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()

    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()