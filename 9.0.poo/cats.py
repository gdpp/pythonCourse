#Given the below class:
from email.policy import compat32


class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Nami', 3)
cat2 = Cat('Sally', 4)
cat3 = Cat('Salem', 2)
cat4 = Cat('Luna', 1)

# 2 Create a function that finds the oldest cat
def find_oldest_cat(catList):
    oldest = max([cat1.age, cat2.age, cat3.age])
    
    return f"The oldest cat is {oldest} years old."

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(find_oldest_cat([cat1, cat2, cat3]))