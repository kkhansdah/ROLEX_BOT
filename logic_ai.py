from collections import Counter, defaultdict

pattern_memory = defaultdict(Counter)

def train_memory(numbers):
    for i in range(len(numbers) - 1):
        curr = int(numbers[i])
        next_num = int(numbers[i + 1])
        pattern_memory[curr][next_num] += 1

def mirror(n):
    mirror_map = {0:9, 1:8, 2:7, 3:6, 4:5, 5:4, 6:3, 7:2, 8:1, 9:0}
    return mirror_map.get(n, n)

def get_prediction(numbers):
    numbers = [int(n) for n in numbers if n.isdigit()]
    if len(numbers) < 5:
        return []

    train_memory(numbers)

    freq = Counter(numbers)
    mirror_scores = Counter()
    gap_scores = Counter()
    modulo_scores = Counter()
    pattern_scores = Counter()

    # GAP logic
    for i in range(len(numbers) - 1):
        gap = abs(numbers[i] - numbers[i + 1])
        gap_scores[gap] += 1

    # Mirror + Modulo logic
    for n in numbers:
        mirror_scores[mirror(n)] += 1
        modulo_scores[n % 3] += 1

    # Pattern logic (based on last number)
    last = numbers[-1]
    for n in pattern_memory[last]:
        pattern_scores[n] += pattern_memory[last][n] * 2

    # Final smart score (no repeat restriction)
    combined_scores = Counter()
    for n in range(10):  # 0 to 9
        combined_scores[n] += freq[n] * 1.2
        combined_scores[n] += mirror_scores[n] * 1.2
        combined_scores[n] += gap_scores[n] * 1.1
        combined_scores[n] += modulo_scores[n % 3] * 1.0
        combined_scores[n] += pattern_scores[n] * 2.5

    top3 = combined_scores.most_common(3)
    return [(num, round(score, 2)) for num, score in top3]
