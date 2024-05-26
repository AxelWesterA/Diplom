import logging
from telegram import _update, _forcereply
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
import django
import os
from django.conf import settings

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from bot.models import Admin, Client

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Команда /start
def start(update: _update, context: CallbackContext) -> None:
    user = update.effective_user
    try:
        admin = Admin.objects.filter(available=True).first()
        if admin:
            admin.available = False
            admin.save()
            client, created = Client.objects.get_or_create(chat_id=user.id)
            client.assigned_admin = admin
            client.save()

            context.bot.send_message(chat_id=admin.chat_id, text=f"Новый клиент: {user.full_name}")
            update.message.reply_text(f"Вы связаны с администратором.")
        else:
            update.message.reply_text(f"К сожалению, сейчас нет свободных администраторов. Попробуйте позже.")
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        update.message.reply_text(f"Произошла ошибка, попробуйте позже.")


# Команда /register_admin
def register_admin(update: _update, context: CallbackContext) -> None:
    user = update.effective_user
    chat_id = user.id
    try:
        admin, created = Admin.objects.get_or_create(chat_id=chat_id)
        admin.available = True
        admin.save()

        update.message.reply_text('Вы зарегистрированы как администратор.')
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        update.message.reply_text(f"Произошла ошибка при регистрации. Попробуйте позже.")


# Обработчик сообщений
def echo(update: _update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)


def main() -> None:
    # Токен вашего бота
    token = 'YOUR_TELEGRAM_BOT_TOKEN'

    # Создаем Updater и передаем ему токен вашего бота
    updater = Updater(token)

    # Получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрируем обработчики
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("register_admin", register_admin))
    dispatcher.add_handler(MessageHandler(filters.text & ~filters.command, echo))

    # Запуск бота
    updater.start_polling()

    # Бот будет работать до тех пор, пока не получит сигнала прерывания
    updater.idle()


if __name__ == '__main__':
    main()
