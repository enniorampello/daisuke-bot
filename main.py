from telegram.ext import Updater, CommandHandler
from polito import Polito
import keys


def start(update, context):
    user_id = update.effective_user.id
    context.bot.send_message(chat_id=user_id, text="I'm a bot, please talk to me!")


updater = Updater(token=keys.get_token())
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()
updater.idle()