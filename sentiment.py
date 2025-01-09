import json
import csv
from konlpy.tag import Okt

# load KNU dictionary
with open('SentiWord_info.json', 'r', encoding='utf-8-sig') as f:
    sentiword_dic = json.load(f)

okt = Okt()

def sentiment(text, dictionary):
    tokens = okt.morphs(text)
    # neutral if not in dictionary
    if not tokens:  
        return 0.0
    
    score = 0
    for entry in dictionary:
        if entry['word'] in tokens or entry['word_root'] in tokens:
            score += int(entry['polarity'])
    
    # scale by dividing by (2 * tokens) to get in range [-1, +1].
    scaled = score / (2.0 * len(tokens))
    return scaled

if __name__ == "__main__":
    file = 'articles_drugs_m.txt'
    
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()

    with open('sentiment_output.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Text", "ScaledSentiment(-1_to_1)"])
        for i, line in enumerate(lines):
            line = line.strip()
            score = sentiment(line, sentiword_dic)
            writer.writerow([line, f"{score:.3f}"])
