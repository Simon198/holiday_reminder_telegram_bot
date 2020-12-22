from datetime import date
import holidays
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update, Bot
import os

dir_path = os.path.abspath(os.path.dirname(__file__))

def getCustomHolidayMessage(holidayName):
    return 'Fröhlichen ' + holidayName + ', ihr Lappen'

def getHolidayName():
    for nationHolidays in [
        holidays.Germany(),
        holidays.India(),
        holidays.Japan(),
        holidays.Mexico(),
        holidays.Russia(),
        holidays.Brazil()
    ]:
        holidayName = nationHolidays.get(date.today())
        if holidayName is not None:
            return holidayName + ' (' + nationHolidays.country + ')'

    return None

def update_chat_ids():
    with open(dir_path + '/TOKEN.txt', 'r') as file:
        token = file.read()

    with open(dir_path + '/CHAT_IDS.txt', 'r') as file:
        chat_ids = file.read().split('\n')

    with open(dir_path + '/OFFSET.txt', 'r') as file:
        offset = int(file.read())

    bot = Bot(token=token)
    updates = bot.get_updates(offset=offset)
    for update in updates:
        message = update.message
        chat_id = str(message.chat_id)
        text = message.text
        latest_offset = update.update_id

        if latest_offset == offset:
            continue

        if (text == '/start' or text == '/start' + bot.name) and chat_id not in chat_ids:
            chat_ids.append(chat_id)
        elif text == '/end' or text == '/end' + bot.name:
            chat_ids.remove(chat_id)

    with open(dir_path + '/CHAT_IDS.txt', 'w') as file:
        file.write('\n'.join(chat_ids))

    with open(dir_path + '/OFFSET.txt', 'w') as file:
        file.write(str(latest_offset))
    
    return bot, chat_ids

def main ():
    bot, chat_ids = update_chat_ids()

    holidayName = getHolidayName()
    if holidayName is None:
        exit()

    custom_message = getCustomHolidayMessage(holidayName)
    for chat_id in chat_ids:
        bot.send_message(chat_id=chat_id, text=custom_message)

if __name__ == '__main__': 
    main()