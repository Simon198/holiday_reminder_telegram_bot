from datetime import date
import holidays
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update, Bot
import os
import json

dir_path = os.path.abspath(os.path.dirname(__file__))

INITIAL_MESSAGE = """Guten Tag,
ich bin ein Bot, der euch an die Feiertage auf eine besondere Weise erinnert.
Meinen Code findet ihr unter: https://github.com/Simon198/holiday_reminder_telegram_bot
"""

with open(dir_path + '/translate.json', 'r') as file:
    translation_dict = json.loads(file.read())

def getCustomHolidayMessage(holidayName, genum='m'):
    customMessage = ''
    if genum == 'm':
        customMessage += 'Fröhlicher'
    elif genum == 'f':
        customMessage += 'Fröhliche'
    elif genum == 'n':
        customMessage += 'Fröhliches'

    return customMessage + ' ' + holidayName + ', ihr Lappen'

def getHoliday():
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
            country = nationHolidays.country
            if holidayName in translation_dict[country]:
                holiday = translation_dict[country][holidayName]
            else:
                holiday = {
                    'translation': holidayName,
                    'genum': 'm'
                }

            if country != 'DE':
                holiday['translation'] += ' (' + country + ')'
            
            return holiday

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

        if text == '/start' or text == '/start' + bot.name:
            bot.send_message(chat_id=chat_id, text=INITIAL_MESSAGE)
            if chat_id not in chat_ids:
                chat_ids.append(chat_id)
        elif text == '/end' or text == '/end' + bot.name:
            chat_ids.remove(chat_id)

    with open(dir_path + '/CHAT_IDS.txt', 'w') as file:
        file.write('\n'.join(chat_ids))

    if len(updates) > 0:
        with open(dir_path + '/OFFSET.txt', 'w') as file:
            file.write(str(latest_offset))
    
    return bot, chat_ids

def main ():
    bot, chat_ids = update_chat_ids()

    holiday = getHoliday()
    if holiday is None:
        exit()

    custom_message = getCustomHolidayMessage(holiday['translation'], holiday['genum'])
    for chat_id in chat_ids:
        bot.send_message(chat_id=chat_id, text=custom_message)

if __name__ == '__main__': 
    main()