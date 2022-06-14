breakfast = ["eggs", "cereal", "banana"]
lunch = ["sushi", "chicken", "soup"]
dinner = ["steak", "meatballs", "pasta"]

print(zip(breakfast, lunch, dinner))
print(type(zip(breakfast, lunch, dinner)))
print(list(zip(breakfast, lunch, dinner)))

for breakfast, lunch, dinner in zip(breakfast, lunch, dinner):
    print(f"My meal for today was {breakfast} and {lunch} and {dinner}")