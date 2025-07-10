from analyzer import analyze_data, predict_numbers

if __name__ == "__main__":
    data_file = "data/history.csv"
    recent_data = analyze_data(data_file)
    prediction, scores = predict_numbers(recent_data)

    print("🔮 Predicted Numbers:")
    for num, score in zip(prediction, scores):
        print(f"Number: {num}, Confidence: {score:.2f}%")
