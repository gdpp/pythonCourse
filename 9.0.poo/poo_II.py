#OOP

class PlayerCharacter:
    #Class Object Attribute
    membership = True
    
    def __init__(self, name, faction):
        if PlayerCharacter.membership:
            #attributes
            self.name = name
            self.faction = faction
    
    def run(self):
        print('run')
        return 'done'
        
    def attack(self, type):
        return (f'Attack type: {type}')
    
    @classmethod
    def adding_health(cls,current_health, plus_health):
        return current_health + plus_health

    @staticmethod
    def adding_armor(current_armor, plus_armor):
        return current_armor + plus_armor
        
timmy = PlayerCharacter('Timmy', 'Elf')
sally = PlayerCharacter('Sally', 'Sorcerer')

print(timmy.name)
print(timmy.run())
print(timmy.attack('fire'))
timmy.attack = 50
print(timmy.attack)
print(sally.name)
print(sally.run())
print(sally.attack('water'))

print(timmy.membership)
print(sally.membership)

print(timmy.adding_health(100, 50))

print(PlayerCharacter.adding_health(300, 100))