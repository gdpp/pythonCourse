cryptocurrencies_prices = {
    "Bitcoin": 400000,
    "Ethereum": 7000,
    "Litecoin": 10
}

# print(cryptocurrencies_prices.keys())
# print(type(cryptocurrencies_prices.keys()))

# print(cryptocurrencies_prices.values())
# print(type(cryptocurrencies_prices.values()))

for currency in cryptocurrencies_prices.keys():
    print(currency)
    
for price in cryptocurrencies_prices.values():
    print(price)
    
print("Bitcoin" in cryptocurrencies_prices.keys())
print("Ripple" in cryptocurrencies_prices.keys())

print(400000 in cryptocurrencies_prices.values())
print(50 in cryptocurrencies_prices.values())

print(len(cryptocurrencies_prices.keys()))
print(len(cryptocurrencies_prices.values()))