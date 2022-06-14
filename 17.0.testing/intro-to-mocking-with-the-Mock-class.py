from unittest.mock import Mock

pizza = Mock()
print(pizza)
print(type(pizza))

pizza.configure_mock(
    size = "Large",
    price = 19.99,
    toppings = ["Pepperoni", "Sausage"]
)

# pizza.size = "Large"
# pizza.price = 19.99
# pizza.toppings = ["Pepperoni", "Sausage"]

print(pizza.size)
print(pizza.price)
print(pizza.toppings)

# print(pizza.anything)

# print(pizza.cover_cheese())
# print(pizza.cover_cheese())