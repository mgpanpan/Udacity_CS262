# This is a set of regular expressions defining a lexer for HTML with embedded
# JavaScript fragments.

import ply.lex as lex

tokens = (
    'LANGLE',         # <
    'LANGLESLASH',    # </
    'RANGLE',         # >
    'SLASHRANGLE',    # /> for the empty tag
    'EQUAL',          # =
    'STRING',         # "str"
    'WORD',           # 'Welcome' in "Welcome to my webpage."
    'JAVASCRIPT',     # embedded JavaScript Fragment
)

# exclusive 独占的 独享的 ==> If I'm in the middle of HTML comment, I can't do
# anything else.
states = (
    ('javascript', 'exclusive'),
    ('htmlcomment', 'exclusive'),
)

def t_htmlcomment(token):
    r'<!--'
    token.lexer.begin('htmlcomment')

def t_htmlcomment_end(token):
    r'-->'
    token.lexer.lineno += token.value.count('\n')
    token.lexer.begin('INITIAL')
    pass

# anything other characters inside html comment are not going to match
# neither of the above two rules, then they are counted as an error.
def t_htmlcomment_error(token):
    token.lexer.skip(1)  # pass
    # skip is a lot like writing "pass" except that it gathers up all of
    # the text into one big value so that I can count the newlines later.
    # look at the htmlcomment_end.

def t_javascript(token):
    r'\<script\ type=\"text\/javascript\"\>'
    token.lexer.code_start = token.lexer.lexpos
    token.lexer.level = 1
    token.lexer.begin('javascript')

def t_javascript_end(token):
    r'</script>'
    token.value = token.lexer.lexdata[token.lexer.code_start:token.lexer.lexpos-9]
    # 9 is the length of string "</script>"
    token.type = "JAVASCRIPT"
    token.lexer.lineno += token.value.count('\n')
    token.lexer.begin('INITIAL')
    return token

def t_javascript_error(token):
    token.lexer.skip(1)

# note, put the LANGLESLASH before LANGLE!!
# so, if I see a left angle followed by a slash, I want it to be a LANGLESLASH
# token and not a LANGLE token followed by a WORD token.
def t_LANGLESLASH(token):
    r'</'
    return token

def t_LANGLE(token):
    r'<'
    return token

def t_SLASHRANGLE(token):
    r'/>'
    return token

def t_RANGLE(token):
    r'>'
    return token

def t_EQUAL(token):
    r'='
    return token

def t_STRING(token):
    r'"(?:[^\\"]|(?:\\.))*"'
    token.value = token.value[1:-1]
    return token

def t_WORD(token):
    r'[^ \t\v\r\n<>=]+'
    return token

t_ignore = ' \t\v\r'  # shortcut for whitespace token
t_htmlcomment_ignore = ' \t\v\r'
t_javascript_ignore = ' \t\v\r'

def t_newline(token):
    r'\n'    # '\\\n'
    token.lexer.lineno += 1
    pass

def t_error(token):
    print("HTML Lexer: Illegal character " + token.value[0])
    token.lexer.skip(1)
