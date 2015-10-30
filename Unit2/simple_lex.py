import ply.lex as lex

tokens = (
    'LANGLE',
    'LANGLESLASH',
    'RANGLE',
    'EQUAL',
    'STRING',
    'WORD',
    'NEWLINE'
)

# exclusive 独占的 独享的 ==> If I'm in the middle of HTML comment, I can't do
# anything else.
states = (
    ('htmlcomment', 'exclusive'),
)

t_ignore = ' '  # shortcut for whitespace token

def t_htmlcomment(token):
    r'<!--'
    token.lexer.begin('htmlcomment')

def t_htmlcomment_end(token):
    r'-->'
    token.lexer.lineno += token.value.count('\n')
    token.lexer.begin('INITIAL')

# anything other characters inside html comment are not going to match
# neither of the above two rules, then they are counted as an error.

def t_htmlcomment_error(token):
    token.lexer.skip(1)  # pass
    # skip is a lot like writing "pass" except that it gathers up all of
    # the text into one big value so that I can count the newlines later.
    # look at the htmlcomment_end.

def t_NEWLINE(token):
    r'\n'    # '\\\n'
    token.lexer.lineno += 1
    pass

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
    r'[^ <>\n]+'
    return token

webpage = "This is <b>my</b> webpage!"

page_newline_test = """ This is
 my webpage.
"""

page_comment_test = "hello <!-- comment --> all"

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

f = open("index.html", "r")
webpage = f.read()

htmllexer.input(webpage)
print("\nTokens of html file index.html")
while True:
    tok = htmllexer.token()
    if tok is None:
        break
    else:
        print(tok)

htmllexer.input(page_newline_test)
print("\ntest of NEWLINE token.html")
while True:
    tok = htmllexer.token()
    if tok is None:
        break
    else:
        print(tok)

htmllexer.input(page_comment_test)
print("\ntest of comment.html")
while True:
    tok = htmllexer.token()
    if tok is None:
        break
    else:
        print(tok)
