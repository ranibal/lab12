import logging
import codecs

from telegram import Update
from telegram.ext import Updater, ComandHandler, MessageHandler, Filters, CallbackContext

# enable logging informacion que vamos a recopilar 

logging.basicConfig(
  format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getlogger(__name__)

tornar = '\n\nTorna al principio y /start\n\n'

# definir comandos handler para que interactue el bot

def start(update, context):
    user = update.effective_user
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'Hola {user.mention_html()}!',
        parse_mode=telegram.ParseMode.HTML
    )

def ayuda(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Este es un bot de ejemplo. Puedes usar el comando /start para comenzar.'
    )

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Agregar comandos y sus manejadores
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('ayuda', ayuda))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
