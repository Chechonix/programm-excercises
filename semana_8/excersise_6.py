import json

filename = "pokemon.json"


with open(filename, "r", encoding="utf-8") as f:
    pokemons = json.load(f)

print("\nEnter information of the new Pokémon:")


name_english = input("Name (English): ")


types_input = input("Type(s) (separate by comma): ")
types = [t.strip() for t in types_input.split(",")]


print("\nBase stats:")
hp = int(input("HP: "))
attack = int(input("Attack: "))
defense = int(input("Defense: "))
sp_attack = int(input("Sp. Attack: "))
sp_defense = int(input("Sp. Defense: "))
speed = int(input("Speed: "))

new_pokemon = {
    "name": {
        "english": name_english
    },
    "type": types,
    "base": {
        "HP": hp,
        "Attack": attack,
        "Defense": defense,
        "Sp. Attack": sp_attack,
        "Sp. Defense": sp_defense,
        "Speed": speed
    }
}


pokemons.append(new_pokemon)

with open(filename, "w", encoding="utf-8") as f:
    json.dump(pokemons, f, indent=4)

print("\nThe Pokémon was added successfully!")
