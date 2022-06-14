consoles = {
    "Sony": "Playstation 5",
    "Microsoft": "Xbox Serie X",
    "Nintendo": "Nintendo Switch",
}

print(consoles.get("Sony"))
print(consoles.get("Nintendo"))

consoles.setdefault("Steam", "Steam Dock")

print(consoles)