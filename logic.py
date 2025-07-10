from collections import defaultdict, Counter

def predict_guaranteed_profit(numbers, profit_numbers):
    scores = defaultdict(int)
    freq = Counter(numbers)

    for i, num in enumerate(numbers):
        scores[num] += freq[num]*10 + max(0,10-i)

        if i >= 2:
            g1 = numbers[i] - numbers[i-1]
            g2 = numbers[i-1] - numbers[i-2]
            if g1 == g2:
                scores[numbers[i] + g1] += 20
            if numbers[i] == numbers[i-1] + numbers[i-2]:
                scores[numbers[i] + numbers[i-1]] += 30

    for p in profit_numbers:
        scores[p] += 50

    top3 = [n for n, _ in sorted(scores.items(), key=lambda x: -x[1])[:3]]

    if not any(n in profit_numbers for n in top3):
        for p in profit_numbers:
            if p in scores:
                top3[-1] = p
                break

    return top3

