# from telegram.ext import Updater
#
# updater = Updater
# git add . --> yaratilgan proyectlarni gitga qoshsin degan buyruq!
# git commit -m ""  --> nmani ozgarganini aytib qoyish qoshtirnoq ichiga "main va requirements fayllar yaratildi"
# git push --> git hubga yuborib qoyish qilingan loyihalarni

# .gitignore --> telegram bot yaratilganda yokida bironta websayt yaratilganda ichidagi tokinla githubga chiqib ketmasligi kerak shu fayl ichida turishi kerak

from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler

updater = Updater(token="6036684924:AAEYUZsmnBetTmOnsOusbc83tGtdzZmH3ZE", use_context=True)  # shu tokenni ish;lat degani

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello New Bot')


dispatcher = updater.dispatcher
add_handler = dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()   # har 10 sekundda yangilanib turadi agar yangilik bosa telegramga yuborib turadi, bomasa shunnchaki ishlab turadi, buning aylanish runtime 10 secund
updater.idle()     # har 10 sekundagi signallarni toxtatib qoyadi
# ctrl + c bosilsa bot ishlashdan toxtedi



