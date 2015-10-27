import re

# Escape Sequences in Python string

a = "P&P is Jane's book"
b = 'P&P is Jane\'s book'

print(a)
print(b)
print(a == b)

aa = """I said, "P&P is Jane's book." """
bb = "I said, \"P&P is Jane's book.\""
print(aa)
print(bb)
print(aa == bb)

aaa = "I said, \"Hello\""
bbb = 'I said, "Hello"'
print(aaa)
print(bbb)
print(aaa == bbb)

print(re.findall("\+\+", "C++ Python"))

# Regular expressions use the backslash character ('\') to indicate
# special forms or to allow special characters to be used without invoking
# their special meaning. This collides with Python’s usage of the same
# character for the same purpose in string literals; for example, to match
#  a literal backslash, one might have to write '\\\\' as the pattern
# string, because the regular expression must be \\, and each backslash
# must be expressed as \\ inside a regular Python string literal.
str = "10\\10\\20"
print(str)
regexp = r"\\"
match = re.findall(regexp, str)
print(match)
print(match[0])
print(match[1])

match_raw = re.findall("\\\\", str)
print(match_raw)
print(match_raw[0])
print(match_raw[1])

f = open("test.txt", "r")
contents = f.read()
print(contents)

regexp = "\\\\section"
print(regexp)
match = re.findall(regexp, contents)
print(match)
print(match[0])

regexp = r"\\section"
print(regexp)
match = re.findall(regexp, contents)
print(match)
print(match[0])

sentence = "Hello       world     Python   "
regexp1 = r"\s+"
regexp2 = "\\s+"
regexp3 = "\s+"

print(re.sub(r"\s+", " ", sentence))
print(re.sub("\\s+", " ", sentence))
print(re.sub("\s+", " ", sentence))

print(regexp1)
print(regexp2)
print(regexp3)
print(regexp1 == regexp2)
print(regexp2 == regexp3)
print("\m")     # \m是不认识的转义序列

regexp = '[a-z]\n'
match = re.findall(regexp, "hello world\n")
print(match)
print(match[0])

regexp = r'[a-z]\n'
match = re.findall(regexp, "hello world\n")
print(match)
print(match[0])
