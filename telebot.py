import logging
import codecs

from telegram import Update
from telegram.ext import Updater, ComandHandler, MessageHandler, Filters, CallbackContext
# enable logging

logging.basicConfig(
  format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
