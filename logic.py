from collections import Counter

def mirror(n):
    mirror_map = {0:9, 1:8, 2:7, 3:6, 4:5, 5:4, 6:3, 7:2, 8:1, 9:0}
    return mirror_map.get(n, n)

def get_prediction(numbers):
    numbers = [int(n) for n in numbers if n.isdigit()]
    freq = Counter(numbers)
    
    mirror_scores = Counter()
    gap_scores = Counter()
    modulo_scores = Counter()

    for i in range(len(numbers)-1):
        gap = abs(numbers[i] - numbers[i+1])
        gap_scores[gap] += 1
    
    for n in numbers:
        m = mirror(n)
        mirror_scores[m] += 1
    
    for n in numbers:
        modulo_scores[n % 3] += 1
    
    combined_scores = Counter()
    for n in range(10):
        combined_scores[n] += freq[n]*2
        combined_scores[n] += mirror_scores[n]*1.5
        combined_scores[n] += gap_scores[n]*1.2
        if n % 3 in modulo_scores:
            combined_scores[n] += modulo_scores[n % 3]

    top3 = combined_scores.most_common(3)
    return [(num, round(score, 1)) for num, score in top3]
