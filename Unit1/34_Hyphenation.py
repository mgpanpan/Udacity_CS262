# Regexp Details and Challenges

import re

# Assign to the variable regexp a Python regular expression that matches
# lowercase words (a-z) or singly-hyphenated lowercase words.

# Hint: It may not be possible to get correctly - do your best!
# after introduce (?:), should do it totally correct.

regexp = r"[a-z]+\-?[a-z]+"

# regexp matches:

print(re.findall(regexp, "well-liked") == ["well-liked"])
#>>> True

print(re.findall(regexp, "html") == ["html"])
#>>> True

print(re.findall(regexp, "a") == ["a"])
#>>> False, not our expected

# regexp does not match:

print(re.findall(regexp, "a-b-c") != ["a-b-c"])
#>>> True

print(re.findall(regexp, "a--b") != ["a--b"])
#>>> True


# final solution
regexp = r"[a-z]+(?:-[a-z]+)?"

print()

print(re.findall(regexp, "well-liked") == ["well-liked"])
#>>> True

print(re.findall(regexp, "html") == ["html"])
#>>> True

print(re.findall(regexp, "a") == ["a"])
#>>> True

# regexp does not match:

print(re.findall(regexp, "a-b-c") != ["a-b-c"])
#>>> True

print(re.findall(regexp, "a--b") != ["a--b"])
#>>> True
