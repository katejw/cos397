from collections import Counter
from konlpy.tag import Okt

def freq(file):
    # read text
    with open(file, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    # tokenize, extract nouns, then count word frequency
    okt = Okt()
    tokens = okt.nouns(text)
    word_counts = Counter(tokens)

    for word, count in word_counts.most_common(15):
        print(f'{word}: {count}')

file = 'character_drugs_m.txt'
freq(file)
