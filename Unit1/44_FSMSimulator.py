# a FSM simulator for regexp r"a+1+"

#
# after drawing the FSM, the edges is obvious
edges = {(1, 'a'): 2,
         (2, 'a'): 2,
         (2, '1'): 3,
         (3, '1'): 3}

accepting = [3]

def fsmsim(string, current, edges, accepting):
    if string == "":  # we already at the end of the input
        return current in accepting
    else:
        letter = string[0]
        if (current, letter) in edges:
            return fsmsim(string[1:], edges[(current, letter)], edges, accepting)
        else:
            return False

print(fsmsim("a1", 1, edges, accepting))
print(fsmsim("aaa111", 1, edges, accepting))
print(fsmsim("a1b", 1, edges, accepting))
print(fsmsim("", 1, edges, accepting))

# Quiz 46
edges = {(1, 'q'): 1}
accepting = [1]
print()
print(fsmsim("", 1, edges, accepting))
print(fsmsim("qqqqqq", 1, edges, accepting))
print(fsmsim("qqqqAqqqq", 1, edges, accepting))

# Quiz 48
edges = {(1, 'a'): 2,
         (1, 'b'): 2,
         (2, 'c'): 3,
         (2, 'd'): 3}
accepting = [2, 3]

print()
print(fsmsim("ac", 1, edges, accepting))
print(fsmsim("aX", 1, edges, accepting))
print(fsmsim("b", 1, edges, accepting))
