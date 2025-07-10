

from telegram.ext import Updater, CommandHandler
from logic import predict_guaranteed_profit
from storage import init_db, get_profit_numbers, set_profit_numbers, log_prediction

BOT_TOKEN = "7600921671:AAEGttPW5TnBd9Y_9KWtKfzn1pX3SklT3oI"

def start(update, context):
    update.message.reply_text("🤖 Welcome! Use /predict and /setprofit.")

def setprofit(update, context):
    user_id = update.message.from_user.id
    try:
        numbers = list(map(int, context.args))
        set_profit_numbers(user_id, numbers)
        update.message.reply_text(f"✅ Profit numbers set: {numbers}")
    except:
        update.message.reply_text("⚠️ Usage: /setprofit 6 9")

def predict(update, context):
    user_id = update.message.from_user.id
    try:
        numbers = list(map(int, context.args))
        if len(numbers) != 10:
            update.message.reply_text("⚠️ Please give exactly 10 numbers.\nExample: /predict 1 2 3 4 5 6 7 8 9 10")
            return

        profit_numbers = get_profit_numbers(user_id)
        result = predict_guaranteed_profit(numbers, profit_numbers)
        log_prediction(user_id, numbers, result)
        msg = (
            f"🔮 Prediction from your 10 numbers:\n"
            f"🔵 Level 1: {result[0]}\n"
            f"🟢 Level 2: {result[1]}\n"
            f"🟣 Level 3: {result[2]}"
        )
        update.message.reply_text(msg)
    except:
        update.message.reply_text("⚠️ Usage: /predict 10_numbers")

def main():
    init_db()
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("setprofit", setprofit))
    dp.add_handler(CommandHandler("predict", predict))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
