from collections import Counter

# def most_frequent_word(text):
#     word = text.split()
#     count = Counter(word)
#     return count.most_common(1)[0]

# print(most_frequent_word("apple banana apple orange banana apple"))

# Least frequent character.
def least_frequent_char(text):
    counts = Counter(text)
    min_count = min(counts.values())
    return [ch for ch, cnt in counts.items() if cnt == min_count]

print(least_frequent_char("hello world"))