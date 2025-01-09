import csv

keywords = [" 인성", "갑질", "민폐", "욕"]

filtered = []
output_file = "character.csv"

with open("top_articles.csv", mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        title, url = row[2], row[3]
        
        for word in keywords:
            if word.lower() in title.lower():
                filtered.append((title, url))

with open(output_file, mode="w", encoding="utf-8", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(filtered)