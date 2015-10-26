# 13
import re
str = "1 + 2 + 3"
digits = re.findall(r"[0-9]", str)
one_two = re.findall(r"[1-2]", str)

print(digits)
print(one_two)
print(re.findall(r"[a-c]", "Barbara Liskov"))

# 14 - 15
print(re.findall(r"[0-9]", "Mir Taqi 1723"))
print(re.findall(r"[A-Z]", "Mir Dard 1721"))
print(re.findall(r"[0-9]", "11 - 7 == 4"))
