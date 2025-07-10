from analyzer import analyze_data

def predict_numbers(file_path):
    top_numbers = analyze_data(file_path)
    if not top_numbers:
        return "No data found."
    return f"Predicted top numbers: {', '.join(top_numbers)}"
