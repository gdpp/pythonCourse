import re

pattern = re.compile(r"([a-zA-Z]).([a])")
string = 'search some string in this string line'

a = pattern.search(string)

print(a)
print(a.span())

print(a.start())
print(a.end())

print(a.group())