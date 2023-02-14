# from telegram.ext import Updater
#
# updater = Updater
# git add . --> yaratilgan proyectlarni gitga qoshsin degan buyruq!
# git commit -m ""  --> nmani ozgarganini aytib qoyish qoshtirnoq ichiga "main va requirements fayllar yaratildi"
# git push --> git hubga yuborib qoyish qilingan loyihalarni
import requests
# .gitignore --> telegram bot yaratilganda yokida bironta websayt yaratilganda ichidagi tokinla githubga chiqib ketmasligi kerak shu fayl ichida turishi kerak

from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from settings import *
from settings.local_settings import TELEGRAM_TOKEN

updater = Updater(token=TELEGRAM_TOKEN, use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text('WikiPedia Botga xush kelibsiz !!!\n'
                              'Sorovingizni /search komandasi orqali kiriting')




def search(update: Update, context: CallbackContext):
    words = context.args
    if len(words) == 0:
        update.message.reply_text("Hech bolmasa /search komandasidan keyin nimadir kiriting!!")
    else:
         search_word = ' '.join(words)
         print(search_word)
         result = requests.get('https://en.wikipedia.org/w/api.php',{
               'action': 'opensearch',
               'search': search_word,
               'limit': 1,
               'namespace': 0,
               'format': 'json'
    })
    result = result.json()
    # print(result[3])
    wiki_link = result[3]
    if len(wiki_link):
        # print(wiki_link[0])
        update.message.reply_text("So'rovingiz bo'yicha quyidagi link topildi\n"
                                  + wiki_link[0])

    else:
        update.message.reply_text("Hechnima topilmadi!!")


dispatcher = updater.dispatcher
add_handler = dispatcher.add_handler(CommandHandler('start', start))
add_handler = dispatcher.add_handler(CommandHandler('search', search))
add_handler = dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=start))  # botga qanaqa buyruq berilsa ham startga olib bor degan buyruq
updater.start_polling()   # har 10 sekundda yangilanib turadi agar yangilik bosa telegramga yuborib turadi, bomasa shunnchaki ishlab turadi, buning aylanish runtime 10 secund
updater.idle()     # har 10 sekundagi signallarni toxtatib qoyadi
# ctrl + c bosilsa bot ishlashdan toxtedi
#
# statlar eng katta mavzu hisoblanadi jhangoda otiladi anonim botlar yasashda kerak boldi



# n = int(input("Enter number: "))
# if n%2 == 1:
#     print("Number is ODD")
# if n%2 == 0:
#     print("Number is EVEN")

# part 1
# new_list = []
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# my_list.sort(reverse=True)
# new_list.append(my_list)
# print(my_list)
#
# new_list = list(range(1, 10))
# new_list = list(range(1, 10, 2))
# print(new_list)
# new_list = list(range(2, 10, 2))
# print(new_list)

# part 3
# forsort = [5, 8, 7, 0, 3, 7, 2, 2, 1]
# forsort.sort()
# print(forsort)
#
# # part 2
# my_list = ["Man", "Tesla", "BMW", "Mersedez", "GM"]






