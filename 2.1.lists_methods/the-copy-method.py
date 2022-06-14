units = ["meter", "kilogram", "second", "ampere", "kelvin", "candela", "mole"]

copy_units = units.copy()

# print(units)
# print(copy_units)

units.remove("kelvin")

print(units)
print(copy_units)

copy_split_units = units[:3].copy()

print(copy_split_units)