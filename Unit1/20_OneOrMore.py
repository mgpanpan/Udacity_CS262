import re

# Maximum match
print(re.findall(r"[0-9]+", "13 from 1 in 1776"))

print(re.findall(r"[0-9] [0-9]+", "a1 2b cc3 44d"))
