from telegram.ext import Updater, CommandHandler
from logic import get_prediction

BOT_TOKEN = "7600921671:AAG3uuoKDA-KWUtVCHwhzkK7K8WCcSfqN9s"

def start(update, context):
    update.message.reply_text("👋 नमस्ते! 10 नंबर भेजो:\nउदाहरण: /predict 5 4 3 2 1 6 8 7 2 3")

def predict(update, context):
    try:
        input_numbers = context.args
        result = get_prediction(input_numbers)
        reply = "🎯 *अगला अनुमानित नंबर (Top 3):*\n\n"
        colors = ["🔵", "🟢", "🟣"]
        for i, (num, score) in enumerate(result):
            reply += f"{colors[i]} Level {i+1}: {num} (Score: {score})\n"
        
        reply += "\n🧠 लॉजिक: Repeat 🔁 + Mirror 🔄 + Gap ↔️ + Modulo ➗\n"
        reply += "📌 Smart Bet: Level 1 या 2\n🔥 Bonus: Try all 3 if confident"
        update.message.reply_text(reply, parse_mode='Markdown')
    except:
        update.message.reply_text("❌ Format गलत है।\nउदाहरण: /predict 5 2 3 7 4 6 1 0 8 9")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("predict", predict))
    updater.start_polling()
    print("🤖 Bot is running...")
    updater.idle()

if __name__ == '__main__':
    main()
