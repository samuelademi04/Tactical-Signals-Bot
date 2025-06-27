from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import random

# Insert your bot token here
TOKEN = "YOUR_BOT_TOKEN_HERE"

# Generate fake signal
def generate_signal(pair):
    rsi = random.randint(25, 75)
    direction = "UP ⬆️" if rsi < 50 else "DOWN ⬇️"
    return f"💱 {pair}\n🕒 Timeframe: 30s\n📊 RSI: {rsi}\n➡️ Sinjal: {direction}"

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("EUR/USD OTC", callback_data='EUR/USD OTC'),
         InlineKeyboardButton("AUD/USD OTC", callback_data='AUD/USD OTC')],
        [InlineKeyboardButton("EUR/JPY OTC", callback_data='EUR/JPY OTC'),
         InlineKeyboardButton("EUR/CHF OTC", callback_data='EUR/CHF OTC')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Zgjedh çiftin për sinjalin:', reply_markup=reply_markup)

# Callback for button presses
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    signal = generate_signal(query.data)
    await query.edit_message_text(text=signal)

# Main function to run the bot
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_callback))
    app.run_polling()

if __name__ == "__main__":
    main()