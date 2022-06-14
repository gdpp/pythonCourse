meals = ["breakfast", "lunch", "dinner"]

print("lunch" in meals)
print("breakfast" in meals)
print("snack" in meals)

print("lunch" not in meals)
print("breakfast" not in meals)
print("snack" not in meals)

test_scores = [99.0, 35.0, 23.5]

print(99.0 in test_scores)
print(99 in test_scores)
print(23.5 in test_scores)
print(27 in test_scores)

print(99.0 not in test_scores)
print(99 not in test_scores)
print(23.5 not in test_scores)
print(27 not in test_scores)

if 1000 not in test_scores:
    print("value not found")
