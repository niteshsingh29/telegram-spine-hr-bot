from typing import Final
from telegram import Update
from telegram.ext import MessageHandler, filters, Application, ContextTypes, CommandHandler

# Bot configuration
TOKEN: Final = '6932311035:AAGZ-2TD1PUOQ9h2WpsGg3uNeO668NGMl2A'
BOT_USERNAME: Final = '@spine_hr_bot'

# Handler for the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.reply_text('Hello! I am your custom bot.')
    except Exception as e:
        print(f"Error in start handler: {e}")

# Function to handle responses based on text
async def handle_response(text: str) -> str:
    try:
        if 'hello' in text:
            return 'Hey Nitesh Here!'
        return 'Sorry, I am not trained for this text. Hahahhaha!'
    except Exception as e:
        print(f"Error in handle_response: {e}")
        return 'An error occurred while processing your request.'

# Handler for processing messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        message_type: str = update.message.chat.type
        text: str = update.message.text

        print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
        response: str = await handle_response(text)

        print('Bot: ', response)
        await update.message.reply_text(response)
    except Exception as e:
        print(f"Error in handle_message: {e}")
        await update.message.reply_text('An error occurred while processing your message.')

# Main function to start the bot
def main():
    try:
        print('Starting Bot...')
        app = Application.builder().token(TOKEN).build()

        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(filters.TEXT, handle_message))

        print('Polling for updates...')
        app.run_polling(poll_interval=1)
    except Exception as e:
        print(f"Error in main: {e}")

if __name__ == '__main__':
    main()