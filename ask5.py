import re
from collections import Counter

filename = './two_cities_ascii.txt'

word_count = Counter()
first2_count = Counter()
first3_count = Counter()
with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = re.sub(r'[^a-zA-Z ]', '', line.lower())
        line = line.split()
        word_count.update(line)
        first2_count.update([word[:2] for word in line if len(word) > 1])
        first3_count.update([word[:3] for word in line if len(word) > 2])

# top 10 words with most counts
print("Top 10 most frequent words:")
for word, count in word_count.most_common(10):
    print("'"+word+"' appears", count, "times.")
print()
# top 3 first two letters
print("Top 3 most frequent first two letters:")
for word, count in first2_count.most_common(3):
    print("'"+word+"' appears", count, "times.")
print()
# top 3 first three letters
print("Top 10 most frequent first three letters:")
for word, count in first3_count.most_common(3):
    print("'"+word+"' appears", count, "times.")
