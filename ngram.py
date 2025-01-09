import re
from konlpy.tag import Okt
from nltk import ngrams
from collections import Counter

def ngram(file, n=2, top_n=20):
    # load file
    with open(file, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    # tokenize to generate n-grams then count frequency
    okt = Okt()
    tokens = okt.morphs(text)
    n_grams = list(ngrams(tokens, n))
    counts = Counter(n_grams)
    most_common_ngrams = counts.most_common(top_n)

    # print results
    for ngram, count in most_common_ngrams:
        print(f"{' '.join(ngram)}: {count}")


file = 'articles_breakup_f.txt'
ngram(file, n=2, top_n=40)
