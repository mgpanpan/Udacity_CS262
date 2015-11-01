grammar = [
    ("S", ["P"]),            # S -> P
    ("P", ["(", "P", ")"]),  # P -> ( P )
    ("P", []),               # P ->
]

tokens = ["(", "(", ")", ")"]

grammar2 = [
    ("P", ["S"]),
    ("S", ["S", "+", "M"]),
    ("S", ["M"]),
    ("M", ["M", "*", "T"]),
    ("M", ["T"]),
    ("T", ["1"]),
    ("T", ["2"]),
    ("T", ["3"]),
    ("T", ["4"]),
]

tokens2 = ["2", "+", "2", "*", "4"]


def addtochart(theset, index, elt):
    if elt in theset[index]:
        return False
    else:
        theset[index] = theset[index] + [elt]
        return True


def closure(grammar, i, x, ab, cd, j):
    next_states = [(cd[0], [], rule[1], i)
                   for rule in grammar if cd != [] and rule[0] == cd[0]]
    return next_states


# 当没有return 或return后面没有返回值时 函数将自动返回None
def shift(tokens, i, x, ab, cd, j):
    if cd != [] and tokens[i] == cd[0]:
        return x, ab + [cd[0]], cd[1:], j


def reductions(chart, i, x, ab, cd, j):
    return [(state[0], state[1] + [x], state[2][1:], state[3])
              for state in chart[j]
              if cd == [] and state[2] != [] and state[2][0] == x]


def parse(tokens, grammar):
    tokens = tokens + ["end_of_input_marker"]
    # because sometimes we need to look ahead, for example, for shifting
    # to see if the input token matches what's there, and we don't want to
    # walk off the end of a list.

    chart = {}

    start_rule = grammar[0]

    for i in range(len(tokens) + 1):
        chart[i] = []

    # state encode : x -> ab . cd from j, ("x", ab, cd, j)
    start_state = (start_rule[0], [], start_rule[1], 0)
    chart[0] = [start_state]

    # consider tokens in the input, and keep using closure, shifting, reduction
    # until there aren't any more changes.

    for i in range(len(tokens)):
        while True:
            changes = False
            for state in chart[i]:
                # State === x -> a b . c d , j
                x = state[0]
                ab = state[1]
                cd = state[2]
                j = state[3]

                # Current State: x -> a b . c d, j
                # Option 1 : For each grammar rule c -> p q r
                # (where the c's match
                # make a next state                c -> . p q r , i
                # We're about to start parsing a "c", but "c" may be something
                # like "exp" with its own production rules. We'll bring those
                # production rules in.
                next_states = closure(grammar, i, x, ab, cd, j)
                for next_state in next_states:
                    changes = addtochart(chart, i, next_state) or changes

                # Current State : x -> a b . c d , j
                # Option 2: If tokens[i] == c,
                # make a next state      x -> a b c . d , j
                # in chart[i+1]
                # We're looking for to parse token c next and the current
                # token is exactly c ! Aren't we lucky! So we can parse over
                # it and move to j + 1.
                next_state = shift(tokens, i, x, ab, cd, j)
                if next_state is not None:
                    any_changes = addtochart(chart, i+1, next_state) or any_changes

                # Current State : x -> a b . c d , j
                # Option 3 : If cd is [], the state is just x -> a b . , j
                # for each p -> q . x r, l in chart[j]
                # make a next state    p -> q x . r, l
                # in chart[i]
                # We just finished parsing an "x" with this token,
                # but that may have been a sub-step (like matching "exp -> 2"
                # in "2+3"). We should update the higher-level rules as well.
                next_states = reductions(chart, i, x, ab, cd, j)
                for next_state in next_states:
                    changes = addtochart(chart, i, next_state) or changes

            # repeating those three procedures until no more changes
            if not changes:
                break


    for i in range(len(tokens)):    # print out the chart
        print("== chart " + str(i))
        for state in chart[i]:
            x = state[0]
            ab = state[1]
            cd = state[2]
            j = state[3]
            print("    " + x + " ->", end="")
            for sym in ab:
                print(" " + sym, end="")
            print(" .", end="")
            for sym in cd:
                print(" " + sym, end="")
            print("  from " + str(j))

    accepting_state = (start_rule[0], start_rule[1], [], 0)
    return accepting_state in chart[len(tokens) - 1]

result = parse(tokens, grammar)

print(result)

print(parse(tokens2, grammar2))
