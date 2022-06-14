pokemon = {
    "Fire": ["Charmander", "Charmeleon", "Charizard"],
    "Water": ["Squirtle", "Warturtle", "Blastoise"],
    "Grass": ["Bulbasaur", "Ivysaur", "Venusaur"]
}

print("Fire" in pokemon)
print("Grass" in pokemon)
print("Electric" in pokemon)

print("Electric" not in pokemon)
print("fire" not in pokemon)
print("Water" not in pokemon)

if "Zombie" in pokemon:
    print(pokemon["Zombie"])
else:
    print("The Zombie category doesn't exist!")