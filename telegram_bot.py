import os
import django
import logging

from asgiref.sync import sync_to_async
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
load_dotenv()


from api.models import Profile

# Logging setup
logging.basicConfig(level=logging.INFO)

# Handle /start command
@sync_to_async
def save_telegram_username(username):
    return Profile.objects.get_or_create(telegram_username=username)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.effective_user.username
    logging.info(f"Received /start from @{username}")

    if username:
        profile, created = await save_telegram_username(username)
        if created:
            await update.message.reply_text(f"👋 Hello @{username}, you've been registered.")
        else:
            await update.message.reply_text(f"👋 Welcome back, @{username}!")
    else:
        await update.message.reply_text("⚠️ You need a Telegram username to register.")

# Main entry point
def main():
    token = os.environ.get('BOT_TOKEN')
    if not token:
        raise Exception("BOT_TOKEN not found in .env file")

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
