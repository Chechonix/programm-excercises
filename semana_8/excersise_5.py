import json

filename = "pokemon.json"


with open(filename, "r", encoding="utf-8") as f:
    pokemons = json.load(f)


print("\nEnter information of the new Pokémon:")
name = input("Name: ")
type_ = input("Type: ")
level = int(input("Level: "))

new_pokemon = {
    "name": name,
    "type": type_,
    "level": level
}


pokemons.append(new_pokemon)


with open(filename, "w", encoding="utf-8") as f:
    json.dump(pokemons, f, indent=4)

print("\nThe Pokémon was added successfully!")
