grammar = [
    ("exp", ["exp", "+", "exp"]),
    ("exp", ["exp", "-", "exp"]),
    ("exp", ["(", "exp", ")"]),
    ("exp", ["num"]),
    ]

# print(grammar)

# start with "a exp", expanded to depth 1:
# "a exp + exp"
# "a exp - exp"
# "a ( exp )"
# "a num"

def expand(tokens, grammar):
    for pos in range(len(tokens)):
        for rule in grammar:
            if rule[0] == tokens[pos]:
                yield tokens[0:pos] + rule[1] + tokens[pos+1:]

depth = 2
utterances = [["a", "exp"]]

for x in range(depth):
    for sentence in utterances:
        utterances = utterances + \
                     [i for i in expand(sentence, grammar)]

for sentence in utterances:
    print(sentence)

print([x*x for x in [1, 2, 3, 4, 5]])
