# a Subset of JavaScript: tokens
import ply.lex as lex

reversed = {
    'else': 'ELSE',
    'false': 'FALSE',
    'function': 'FUNCTION',
    'if': 'IF',
    'return': 'RETURN',
    'true': 'TRUE',
    'var': 'VAR'
}

tokens = (
        'ANDAND',       # &&
        'COMMA',        # ,
        'DIVIDE',       # /
        # 'ELSE',         # else
        'EQUAL',        # =
        'EQUALEQUAL',   # ==
        # 'FALSE',        # false
        # 'FUNCTION',     # function
        'GE',           # >=
        'GT',           # >
        'IDENTIFIER',   #
        # 'IF',           # if
        'LBRACE',       # {
        'LE',           # <=
        'LPAREN',       # (
        'LT',           # <
        'MINUS',        # -
        'NOT',          # !
        'NUMBER',       #
        'OROR',         # ||
        'PLUS',         # +
        'RBRACE',       # }
        # 'RETURN',       # return
        'RPAREN',       # )
        'SEMICOLON',    # ;
        'STRING',       #
        'TIMES',        # *
        # 'TRUE',         # true
        # 'VAR',          # var
) + tuple(reversed.values())

#
# Write your code here.
#
states = (
    ('comment', 'exclusive'),
)

def t_comment(token):
    r'/\*'
    token.lexer.begin('comment')

def t_comment_end(token):
    r'\*/'
    token.lexer.lineno += token.value.count('\n')
    token.lexer.begin('INITIAL')
    pass

def t_comment_error(token):
    token.lexer.skip(1)

t_comment_ignore = r' \t\v\r'

def t_eolcomment(token):
    r'//.*'
    pass

t_ANDAND = r'&&'
t_COMMA = r','
t_DIVIDE = r'/'
t_EQUALEQUAL = r'=='
t_EQUAL = r'='
t_GE = r'>='
t_GT = r'>'
t_LBRACE = r'{'
t_LE = r'<='
t_LPAREN = r'\('
t_LT = r'<'
t_MINUS = r'-'
t_NOT = r'!'
t_OROR = r'\|\|'
t_PLUS = r'\+'
t_RBRACE = r'}'
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_TIMES = r'\*'

# characters in identifiers can have numbers
def t_IDENTIFIER(token):
    r'[a-zA-Z][a-zA-z_0-9]*'
    token.type = reversed.get(token.value, 'IDENTIFIER')
    return token

def t_NUMBER(token):
    r'-?[0-9]+(?:\.[0-9]*)?'
    token.value = float(token.value)
    return token

def t_STRING(token):
    r'"(?:[^\\"]|(?:\\.))*"'
    token.value = token.value[1:-1]
    return token

t_ignore = ' \t\v\r'  # whitespace

def t_newline(t):
    r'\n'
    t.lexer.lineno += 1

def t_error(t):
    print("JavaScript Lexer: Illegal character " + t.value[0])
    t.lexer.skip(1)

## unit test

# We have included two test cases to help you debug your lexer. You will
# probably want to write some of your own.
# lexer = lex.lex()
#
# def test_lexer(input_string):
#     lexer.input(input_string)
#     result = [ ]
#     while True:
#         tok = lexer.token()
#         if not tok: break
#         result = result + [(tok.type, tok.value)]
#     return result
#
# input1 = """ - !  && () * , / ; { || } + < <= = == > >= else false function
# if return true var vary n-1"""
#
# output1 = ['MINUS', 'NOT', 'ANDAND', 'LPAREN', 'RPAREN', 'TIMES', 'COMMA',
# 'DIVIDE', 'SEMICOLON', 'LBRACE', 'OROR', 'RBRACE', 'PLUS', 'LT', 'LE',
# 'EQUAL', 'EQUALEQUAL', 'GT', 'GE', 'ELSE', 'FALSE', 'FUNCTION', 'IF',
# 'RETURN', 'TRUE', 'VAR', 'IDENTIFIER']
#
#print(test_lexer(input1))
#
# input2 = """
# if // else mystery
# =/*=*/=
# true /* false
# */ return"""
#
# output2 = ['IF', 'EQUAL', 'EQUAL', 'TRUE', 'RETURN']
#
# print(test_lexer(input2) == output2)
