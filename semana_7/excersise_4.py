import csv

filename = "videogames_tab.tsv"

fieldnames = ["name", "genre", "developer", "esrb_rating"]

n = int(input("How many videogames do you want to enter? "))

rows = []

for i in range(n):
    print(f"\nVideogame #{i + 1}")
    name = input("Name: ")
    genre = input("Genre: ")
    developer = input("Developer: ")
    esrb = input("ESRB rating: ")

    rows.append({
        "name": name,
        "genre": genre,
        "developer": developer,
        "esrb_rating": esrb
    })

with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t")
    writer.writeheader()
    for row in rows:
        writer.writerow(row)

print(f"\nData successfully saved in {filename}")
