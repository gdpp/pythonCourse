#name, adjetive, noun
# mad_libs = "{} laughed at the {} {}"

# print(mad_libs.format("Leslie", "Green", "Alien"))
# print(mad_libs.format("Gustavo", "Silly", "Tomato"))


# mad_libs = "{2} laughed at the {1} {0}"

# print(mad_libs.format("Leslie", "Green", "Alien"))
# print(mad_libs.format("Gustavo", "Silly", "Tomato"))


mad_libs = "{name} laughed at the {adj} {noun}"

# print(mad_libs.format(name = "Leslie", adj = "Green", noun = "Alien"))
# print(mad_libs.format(name = "Gustavo", adj = "Silly", noun = "Tomato"))

name = input("Enter a name: ")
adjetive = input("Enter adjetive: ")
noun = input("Enter noun: ")

print(mad_libs.format(name = name, adj = adjetive, noun = noun))

