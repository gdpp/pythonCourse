import re

pattern = re.compile(r"[A-za-z0-9#$%@]{8,}\d")

password = 'secretpass#$6'

a = pattern.search(password)

check = pattern.fullmatch(password)

