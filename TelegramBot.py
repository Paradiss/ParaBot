from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem
from datetime import datetime, date, time

logging.basicConfig(format='%(asktime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def constellation(bot, update):
    user_text = update.message.text 
    user_text_list = user_text.split()
    planet = user_text_list[1]
    if planet.lower() == 'mars':
        mars = ephem.Mars()  
        mars.compute(datetime.today().strftime('%Y/%m/%d'))
        print(ephem.constellation(mars))
        update.message.reply_text(ephem.constellation(mars))

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    logging.info('Бот запускается')

    mars = ephem.Mars()  
    mars.compute(datetime.today().strftime('%Y/%m/%d'))
    print(ephem.constellation(mars))

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", constellation))

    mybot.start_polling()
    mybot.idle()

main()
