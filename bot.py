import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure the generative model
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

def generate_content(full_prompt: str) -> str:
    try:
        response = model.generate_content(full_prompt)
        return response.text if hasattr(response, 'text') else "Sorry, I couldn't generate a response."
    except Exception as e:
        return f"There was an error generating the response: {str(e)}"

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
