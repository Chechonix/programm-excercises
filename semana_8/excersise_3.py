import csv

filename = "videogames.csv"

n = int(input("How many videogames do you want to enter? "))

rows = []

for i in range(n):
    print(f"\nVideogame #{i + 1}")
    name = input("Name: ")
    genre = input("Genre: ")
    developer = input("Developer: ")
    esrb = input("ESRB rating: ")

    rows.append([name, genre, developer, esrb])

with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "genre", "developer", "esrb_rating"])
    writer.writerows(rows)

print(f"\nData successfully saved in {filename}")
