import csv

# keywords to look for
keywords = [" 인성", "갑질", "민폐", "욕"]

filtered = []
output = "character.csv"

# put title in csv if it contains keyword
with open("top_articles.csv", mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        title, url = row[2], row[3]
        
        for word in keywords:
            if word.lower() in title.lower():
                filtered.append((title, url))

with open(output, mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(filtered)
