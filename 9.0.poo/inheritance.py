class User():
    def __init__(self, email):
        self.email = email
        
    def sign_in(self):
        print('Log in')
        
class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'Attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with arrows: arrows left - {self.num_arrows}')
        
        
wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)

print(wizard1.sign_in())

print(wizard1.attack())
print(archer1.attack())

print(isinstance(wizard1, object))