import telebot
from analyzer import analyze_data, predict_numbers

TOKEN = "7600921671:AAEjzC9LlJXGYLNg4B__hnL8s5XujKzo6ME"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "🔮 Welcome to KWG Predictor Bot!\nSend /predict to get 3 lucky numbers.")

@bot.message_handler(commands=['predict'])
def predict(message):
    try:
        data_file = "data/history.csv"
        data = analyze_data(data_file)
        prediction, scores = predict_numbers(data)

        result = "🎯 Predicted Numbers:\n"
        for num, score in zip(prediction, scores):
            result += f"➡️ {num} (Confidence: {score:.2f}%)\n"

        bot.reply_to(message, result)
    except Exception as e:
        bot.reply_to(message, f"❌ Error: {str(e)}")

bot.polling()
