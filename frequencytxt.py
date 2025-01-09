from collections import Counter
from konlpy.tag import Okt

def freq(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    okt = Okt()
    # extract nouns
    tokens = okt.nouns(text)
    # count word frequency
    word_counts = Counter(tokens)

    for word, count in word_counts.most_common(15):
        print(f'{word}: {count}')

file_path = 'character_drugs_m.txt'
freq(file_path)
