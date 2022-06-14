class Pokemon():
    def __init__(self, name, specialty, health):
        self.name = name
        self.specialty = specialty
        self.health = health
    
    def roar(self):
        print("Raaaaaarr!")
        
    def describe_pokemon(self):
        print(f"I am { self.name }. I am a { self.specialty } Pokemon.")
    
    def take_damage(self, damage):
        self.health -= damage

squirtle = Pokemon("Squirtle", "Water", 100)
charmander = Pokemon(name = "Charmander", specialty = "Fire", health = 110)

squirtle.roar()
charmander.roar()

squirtle.describe_pokemon()
charmander.describe_pokemon()

print(squirtle.health)
squirtle.take_damage(20)
print(squirtle.health)