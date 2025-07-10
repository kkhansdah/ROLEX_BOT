from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from logic_ai import get_prediction

BOT_TOKEN = "7600921671:AAG3uuoKDA-KWUtVCHwhzkK7K8WCcSfqN9s"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Welcome to AI Number Prediction Bot!\nSend 10 numbers using /predict command.")

async def predict(update: Update, context: ContextTypes.DEFAULT_TYPE):
    numbers = context.args
    if len(numbers) != 10:
        await update.message.reply_text("❗ Please send exactly 10 numbers.\nExample:\n/predict 3 1 4 5 9 2 6 8 7 0")
        return

    prediction = get_prediction(numbers)
    if not prediction:
        await update.message.reply_text("❌ Invalid input or not enough data.")
        return

    msg = "🎯 Predicted Top 3 Numbers:\n\n"
    levels = ["🔵 Level 1", "🟢 Level 2", "🟣 Level 3"]

    for i, (num, score) in enumerate(prediction):
        msg += f"{levels[i]}: {num} (Score: {score})\n"

    msg += "\n🧠 Logic: AI Pattern + Mirror + Modulo + Gap\n🔥 Risk Level: Low"
    await update.message.reply_text(msg)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("predict", predict))
print("🤖 Bot is running...")
app.run_polling()
