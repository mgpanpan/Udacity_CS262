# Bonus Practice: Find Max

# This assignment is not graded and we encourage you to experiment. Learning is
# fun!

# Given a list l and a function f, return the element of l that maximizes f.

# Assume:
#    l is not empty
#    f returns a number

# Example:

l = ['Barbara', 'kingsolver', 'wrote', 'The', 'Poisonwood','Bible']
f = len

# Try it on your own!
def findmax(f, l):
    max_value = None
    max_elem = None
    for elem in l:
        if max_value is None or f(elem) > max_value:
            max_elem = elem
            max_value = f(elem)
    return max_elem

print(findmax(f, l))




