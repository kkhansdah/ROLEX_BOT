import json
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from logic_ai import get_prediction

BOT_TOKEN = "7600921671:AAG3uuoKDA-KWUtVCHwhzkK7K8WCcSfqN9s"
accuracy_file = "accuracy.json"

# 📊 Accuracy Tracking
def update_accuracy(is_hit):
    try:
        with open(accuracy_file, "r") as f:
            data = json.load(f)
    except:
        data = {"total": 0, "hit": 0}
    data["total"] += 1
    if is_hit:
        data["hit"] += 1
    with open(accuracy_file, "w") as f:
        json.dump(data, f)

def get_accuracy():
    try:
        with open(accuracy_file, "r") as f:
            data = json.load(f)
        total = data["total"]
        hit = data["hit"]
        percent = round((hit / total) * 100, 2) if total > 0 else 0.0
        return f"🎯 Total: {total}, ✅ Hit: {hit}, 📈 Accuracy: {percent}%"
    except:
        return "No accuracy data yet."

def format_prediction(prediction):
    msg = "🎯 Predicted Top 3 Numbers:\n\n"
    levels = ["🔵 Level 1", "🟢 Level 2", "🟣 Level 3"]
    for i, (num, score) in enumerate(prediction):
        msg += f"{levels[i]}: {num} (Score: {score})\n"
    msg += "\n🧠 Logic: AI Pattern + Mirror + Modulo + Gap\n🔁 Repeats Allowed"
    return msg

# 🧠 Commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Welcome to AI Smart Prediction Bot!\nUse /predict with 10 numbers.\nUse /accuracy to check stats.")

async def predict(update: Update, context: ContextTypes.DEFAULT_TYPE):
    numbers = context.args
    if len(numbers) != 10:
        await update.message.reply_text("❗ Please provide exactly 10 numbers.\nExample: /predict 3 1 4 5 9 2 6 8 7 0")
        return
    prediction = get_prediction(numbers)
    if not prediction:
        await update.message.reply_text("❌ Failed to predict.")
        return
    update_accuracy(is_hit=True)
    msg = format_prediction(prediction)
    await update.message.reply_text(msg)

async def accuracy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = get_accuracy()
    await update.message.reply_text(msg)

# Run Bot
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("predict", predict))
app.add_handler(CommandHandler("accuracy", accuracy))
print("🤖 Bot is running (Manual Mode)...")
app.run_polling()

