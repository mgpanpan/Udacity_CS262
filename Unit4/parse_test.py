# QUIZ

# JavaScript allows function calls:
#   myfun(11,12)

# We want the parse tree to be:
#   ("call", "myfun", [("number", 11), ("number", 12)])

import jstokens
import ply.lex as lex
import ply.yacc as yacc

start = 'exp'

precedence = (
        ('left', 'OROR'),
        ('left', 'ANDAND'),
        ('left', 'EQUALEQUAL'),
        ('left', 'LT', 'LE', 'GT', 'GE'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE'),
        ('right', 'NOT'),
)

tokens = jstokens.tokens

def p_exp_call(p):
    'exp : IDENTIFIER LPAREN optargs RPAREN'
    p[0] = ("call", p[1], p[3])

def p_exp_number(p):
    'exp : NUMBER'
    p[0] = ("number", p[1])

def p_optargs(p):
    'optargs : args'
    p[0] = p[1] # the work happens in "args"

def p_optargsempty(p):
    'optargs : '
    p[0] = [] # no arguments -> return the empy list

def p_args(p):
    'args : exp COMMA args'
    p[0] = [p[1]] + p[3]

def p_args_last(p): # one argument
    'args : exp'
    p[0] = [p[1]]

def p_error(p):
    print("Syntax error in input!")

# here's some code to test with
jslexer = lex.lex(module=jstokens)

jsparser = yacc.yacc()
jsast = jsparser.parse("myfun(11,12,13)",lexer=jslexer)
print(jsast)
