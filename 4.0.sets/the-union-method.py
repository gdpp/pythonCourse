candy_bars = { "Milky Way", "Snickers", "100 Grand" }
sweet_thing = { "Sour Patch Kids", "Reeses Pieces", "Snickers" }

print(candy_bars.union(sweet_thing))
print(sweet_thing.union(candy_bars))

print(sweet_thing | candy_bars)