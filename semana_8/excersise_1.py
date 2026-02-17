input_file = "songs.txt"

output_file = "sorted_songs.txt"

with open(input_file, "r", encoding="utf-8") as f:
    songs = f.readlines()

clean_songs = [song.strip() for song in songs]
sorted_songs = sorted(clean_songs)

with open(output_file, "w", encoding="utf-8") as f:
    for song in sorted_songs:
        f.write(song + "\n")

print("🎵 Songs have been sorted and saved in", output_file)