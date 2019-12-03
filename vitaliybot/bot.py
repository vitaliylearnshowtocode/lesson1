from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
use_context = True
import logging
import ephem

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

planets_dict = {
                "Меркурий" : ephem.Mercury,
                "Венера" : ephem.Venus, 
                "Марс" : ephem.Mars, 
                "Mars" : ephem.Mars, 
                "Юпитер" : ephem.Jupiter, 
                "Сатурн" : ephem.Saturn, 
                "Уран" : ephem.Uranus, 
                "Нептун" :ephem.Neptune, 
                "Плутон" : ephem.Pluto, 
                "Луна" : ephem.Moon } 


def planet(bot, update):
    planet_user_whant = update.message.text.split()[1] #Переменная = планета, которой интересуется пользователь
    planet_name = planets_dict[planet_user_whant] #Переменная = содержимое словаря ephem
    
    #если ввести неверное название планеты на 30 строки все ломается. Как поправить?
    #File "C:\projects\lesson1\vitaliybot\bot.py", line 30, in planet
    #planet_name = planets_dict[planet_user_whant] #Переменная = содержимое словаря ephem
#KeyError: 'эээээ'

    if planet_user_whant in planets_dict:
        date_for_planet = planet_name(update.message.date)
        const = ephem.constellation(date_for_planet)
        update.message.reply_text(const)
    
    else:
        update.message.reply_text("Про планету {} я ничего не знаю".format(planet_user_whant))

def greet_user(bot, update):
    text ='Вызван /start'
    print(text)
    logging.info(text)
    update.message.reply_text(text)
    
def talk_to_me(bot, update):
    user_text = "Привет {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text) 
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username,
                update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)
   
def main():
    mybot = Updater("1022326450:AAFWDVOp2PLin8UUenv61C6qZpHfTrYkMD8", request_kwargs=PROXY)
    
    logging.info('Бот запускается')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me, planet))
    dp.add_handler(CommandHandler("planet", planet))


    mybot.start_polling()
    mybot.idle()

main()
