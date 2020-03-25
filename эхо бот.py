# Импортируем необходимые классы.
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler


# Определяем функцию-обработчик сообщений.
# У неё два параметра, сам бот и класс updater, принявший сообщение.
def echo(update, context):
    # У объекта класса Updater есть поле message,
    # являющееся объектом сообщения.
    # У message есть поле text, содержащее текст полученного сообщения,
    # а также метод reply_text(str),
    # отсылающий ответ пользователю, от которого получено сообщение.
    update.message.reply_text(f'Я получил сообщение {update.message.text}')


def main():
    REQUEST_KWARGS = {
        'proxy_url': 'socks5://ip:port',  # Адрес прокси сервера
        # Опционально, если требуется аутентификация:
        # 'urllib3_proxy_kwargs': {
        #     'assert_hostname': 'False',
        #     'cert_reqs': 'CERT_NONE'
        #     'username': 'user',
        #     'password': 'password'
        # }
    }

    updater = Updater('1102656386:AAGo4YmEWgfo6z-x0qMtLKo5occ_RLp9w2o', use_context=True,
                      request_kwargs=REQUEST_KWARGS)
    # Создаём объект updater.
    # Вместо слова "TOKEN" надо разместить полученный от @BotFather токен

    # Получаем из него диспетчер сообщений.
    dp = updater.dispatcher

    # Создаём обработчик сообщений типа Filters.text
    # из описанной выше функции echo()
    # После регистрации обработчика в диспетчере
    # эта функция будет вызываться при получении сообщения
    # с типом "текст", т. е. текстовых сообщений.
    text_handler = MessageHandler(Filters.text, echo)

    # Регистрируем обработчик в диспетчере.
    dp.add_handler(text_handler)
    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()

    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()