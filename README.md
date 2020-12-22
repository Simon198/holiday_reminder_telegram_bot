# holiday_reminder_telegram_bot
The project implements a [Telegram bot](https://github.com/python-telegram-bot/python-telegram-bot) that sends special messages to all subscribers on holidays.

## Getting started
To run the bot, you need to create a new Telegram bot with the help of the BotFather and store the token in a TOKEN.txt file. Also you need to create two empty txt-files: OFFSET and CHAT_IDS. Afterwards, you have run ```
python3 reminder.py
``` once a day.

## How it works
When a user executes the /start command, the bot stores its chat-id. By executing /end, the chat-id will be removed. When the bot is started on a holiday, a custom message is sent to all chat-ids.