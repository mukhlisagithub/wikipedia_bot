import requests
from telegram import Update,  InlineKeyboardButton, InlineKeyboardMarkup
from telegram.text import Updater, CommandHandler, CallbackContext
from settings import *

updater = Updater