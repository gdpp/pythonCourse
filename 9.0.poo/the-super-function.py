class Animal():
    def __init__(self, name):
        self.name = name
        
    def eat(self, food):
        return f"{ self.name } is enjoying the { food }"
    
    
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

watsons = Dog("Watson", "Golden Retriever")
print(watsons.name)
print(watsons.breed)