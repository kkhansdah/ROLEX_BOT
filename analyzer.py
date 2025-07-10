import csv

def analyze_data(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)

    if len(data) < 2:
        return []

    # Remove header
    rows = data[1:]

    # Extract last column
    last_col_index = len(rows[0]) - 1
    last_numbers = [int(row[last_col_index]) for row in rows if row[last_col_index].isdigit()]

    # Get most common numbers
    freq = {}
    for num in last_numbers:
        freq[num] = freq.get(num, 0) + 1

    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    top_5 = [str(num[0]) for num in sorted_freq[:5]]

    return top_5

