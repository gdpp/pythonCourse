class Guitar():
    def __init__(self):
        print(f"A new guitar is being created! This object is { self }")
    
acoustic = Guitar()
print(acoustic)

electric = Guitar()
print(electric)

acoustic.wood = "Mahogany"
acoustic.string = 6
acoustic.year = 1990

electric.nickname = "Sound Viking 3000"

print(acoustic.wood)
print(electric.nickname)
