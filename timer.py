# Импортируем необходимые классы.
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
import time


# Обычный обработчик, как и те, которыми мы пользовались раньше.
def set_timer(bot, update, job_queue, chat_data, args):
    """Добавляем задачу в очередь"""
    chat_id = update.message.chat_id
    try:
            # создаем задачу task в очереди job_queue через 20 секунд
            # передаем ей идентификатор текущего чата (будет доступен через job.context)

        delay = int(args[0]) if len(args) > 0 else 5  # секунд

        job = job_queue.run_once(task, delay, context=update.message.chat_id)

        # Запоминаем в пользовательских данных созданную задачу.
        chat_data['job'] = job

        # Присылаем сообщение о том, что все получилось.
        update.message.reply_text('Вернусь через {delay} секунд!'.format(**locals()))

        if delay < 0:
            update.message.reply_text(
                'Извините, не умеем возвращаться в прошлое')
            return
    except (IndexError, ValueError):
        update.message.reply_text('Использование: /set <секунд>')


def task(context):
    job = context.job
    context.bot.send_message(job.context, text='Вернулся!')


def help(update, context):
    update.message.reply_text(
        "Я пока не умею помогать... Я только ваше эхо.")


def time_1(update, context):
    t = ' '.join(str(time.asctime()).split()[1:3]) + str(str(time.asctime()).split()[-1])
    update.message.reply_text(t)


def date(update, context):
    update.message.reply_text(str(time.asctime()).split()[-2])


def unset_timer(update, context):
    # Проверяем, что задача ставилась
    if 'job' not in context.chat_data:
        update.message.reply_text('Нет активного таймера')
        return
    job = context.chat_data['job']
    # планируем удаление задачи (выполнится, когда будет возможность)
    job.schedule_removal()
    # и очищаем пользовательские данные
    del context.chat_data['job']
    update.message.reply_text('Хорошо, вернулся сейчас!')

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

    dp.add_handler(CommandHandler("set_timer", set_timer, pass_job_queue=True, pass_chat_data=True, pass_args=True))
    dp.add_handler(CommandHandler("unset_timer", unset_timer, pass_chat_data=True))
    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()

    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()


