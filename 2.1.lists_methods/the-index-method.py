pizzas = [
    "Pepperoni",
    "Sausage",
    "Mushroom",
    "Pepperoni",
    "Sausage"
]

print(pizzas.index("Mushroom"))
print(pizzas.index("Pepperoni"))

if "Olives" in pizzas:
    print(pizzas.index("Olives"))
else:
    print("Not exists")    

print(pizzas.index("Pepperoni", 2))