import pandas as pd
from collections import Counter

def analyze_data(filepath):
    df = pd.read_csv(filepath)
    return list(df['Number'].tail(100))  # last 100 rounds

def score_number(num, freq, gap, total_rounds):
    freq_score = (1 - (freq.get(num, 0) / total_rounds)) * 50
    gap_score = min(gap.get(num, 1), 10) * 5
    return freq_score + gap_score

def predict_numbers(numbers):
    total_rounds = len(numbers)
    freq = Counter(numbers)

    # Calculate gap since last occurrence
    gap = {}
    for i in range(1, 10):
        if i in numbers[::-1]:
            gap[i] = numbers[::-1].index(i) + 1
        else:
            gap[i] = total_rounds + 1

    # Score each number
    scores = {i: score_number(i, freq, gap, total_rounds) for i in range(1, 10)}
    sorted_nums = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    prediction = [n[0] for n in sorted_nums[:3]]
    confidence = [n[1] for n in sorted_nums[:3]]
    return prediction, confidence
