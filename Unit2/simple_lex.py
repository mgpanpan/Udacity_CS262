import ply.lex as lex

tokens = (
    'LANGLE',
    'LANGLESLASH',
    'RANGLE',
    'EQUAL',
    'STRING',
    'WORD',
)

t_ignore = ' '  # shortcut for whitespace token

# note, put the LANGLESLASH before LANGLE!!
# so, if I see a left angle followed by a slash, I want it to be a LANGLESLASH
# token and not a LANGLE token followed by a WORD token.
def t_LANGLESLASH(token):
    r'</'
    return token

def t_LANGLE(token):
    r'<'
    return token

def t_RANGLE(token):
    r'>'
    return token

def t_EQUAL(token):
    r'='
    return token

def t_STRING(token):
    r'"[^"]*"'
    token.value = token.value[1:-1]
    return token

def t_WORD(token):
    r'[^ <>]+'
    return token

webpage = "This is <b>my</b> webpage!"


# this function call tells our lexical analysis library that we want to use
# all of the token definitions above to make a lexical analyzer and break up strings.
htmllexer = lex.lex()
htmllexer.input(webpage)

while True:
    tok = htmllexer.token()
    if tok is None:
        break
    else:
        print(tok)

f = open("test.html", "r")
webpage = f.read()

htmllexer.input(webpage)
print("\nTokens of html file test.html")
while True:
    tok = htmllexer.token()
    if tok is not None:
        print(tok)
