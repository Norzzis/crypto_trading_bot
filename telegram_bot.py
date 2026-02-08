import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Initialize the Telegram Bot
BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'
CHAT_ID = 'YOUR_CHAT_ID_HERE'  # Replace with the target chat ID

bot = telegram.Bot(token=BOT_TOKEN)

def start(update, context):
    update.message.reply_text('Hello! I am your Crypto Trading Bot.')

def send_signal(signal):
    try:
        bot.send_message(chat_id=CHAT_ID, text=f"New trading signal: {signal}")
    except telegram.error.TelegramError as e:
        print(f"Error sending message: {e}")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()