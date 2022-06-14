empty_space = "        content           "

print(empty_space.rstrip())
print(len(empty_space.rstrip()))

print(empty_space.lstrip())
print(len(empty_space.lstrip()))

print(empty_space.strip())
print(len(empty_space.strip()))

website = "www.python.org"

print(website.strip("w"))
print(len(website.strip("w")))

print(website.lstrip("w"))
print(len(website.lstrip("w")))

print(website.rstrip("org"))
print(len(website.rstrip("org")))

print(website.strip("worg"))
print(len(website.strip("worg")))