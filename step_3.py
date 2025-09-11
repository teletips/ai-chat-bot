import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

def generate_content(full_prompt: str) -> str:
    response = full_prompt
    return response

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.first_name
    system_message = f"Hello {user_id}! I am a chatbot. How can I help you today?"
    await update.message.reply_text(system_message)

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    response_text = generate_content(user_message)
    await update.message.reply_text(response_text)

# Build the application
app = ApplicationBuilder().token(TOKEN).build()

# Add handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

# Run the bot
app.run_polling()
