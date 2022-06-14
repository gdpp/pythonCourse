mountains = ["everest", "K2"]
print(mountains)

mountains.extend(["Kangchenjunga", "Lhotse", "Makalu"])
print(mountains)

extra_mountains = ["Orizaba", "Dante"]
mountains.extend(extra_mountains)
print(mountains)

mountains = mountains + extra_mountains
print(mountains)