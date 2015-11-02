# 39 Quoted Strings && 41 Escaping the Escape
import re

f = open("quotedstrings.txt", "r")
contents = f.read()
print(contents)

# solution
regexp = r'"(?:[^\\\"]|(?:\\.))*"'

match = re.findall(regexp, contents)
print(match)
print(match[0])
print(match == [contents])
print()

s1 = '"You say, \\"yes\\", I say \\"no.\\""'
print(s1)
print(re.findall(regexp, s1) == [s1])
print()

s2 = '"I dont know why you say, \\"goodbye.\\""'
print(s2)
print(re.findall(regexp, s2) == [s2])
print()

s3 = '"I say, \\"hello.\\"'
print(s3)
print(re.findall(regexp, s3) == [s3])

s4 = '"hello" == "world"'
s4_out = re.findall(regexp, s4);
print(s4_out)

# dot/period (.)
# print(re.findall("[0-9].[0-9]", "1a1 222 cc3"))

# ^
# print(re.findall("[0-9][^ab]", "1a1 222 cc3"))
