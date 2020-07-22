from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def getdog(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater('1372799976:AAHVABYilv-pezbU4ZebIIcfFdE77zaB6LY')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('getdog',getdog))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()