import jstokens
import ply.lex as lex
import ply.yacc as yacc

from jstokens import tokens

start = 'js'

precedence = (
    ('left', 'OROR'),
    ('left', 'ANDAND'),
    ('left', 'EQUALEQUAL'),
    ('left', 'LT', 'LE', 'GT', 'GE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'NOT'),
)

def p_js_element(p):
    'js : element js'
    p[0] = [p[1]] + p[2]

def p_js_empty(p):
    'js : '
    p[0] = []

def p_element_function_define(p):
    'element : FUNCTION IDENTIFIER LPAREN optparams RPAREN compoundstmt'
    p[0] = ("function", p[2], p[4], p[6])

def p_element_statement(p):
    'element : stmt SEMICOLON'
    p[0] = ("stmt", p[1])

def p_optparams_params(p):
    'optparams : params'
    p[0] = p[1]

def p_optparams_empty(p):
    'optparams : '
    p[0] = []

def p_params(p):
    'params : IDENTIFIER COMMA params'
    p[0] = [p[1]] + p[3]

def p_params_last(p):
    'params : IDENTIFIER'
    p[0] = [p[1]]

def p_compoundstmt(p):
    'compoundstmt : LBRACE statements RBRACE'
    p[0] = p[2]

def p_statements(p):
    'statements : stmt SEMICOLON statements'
    p[0] = [p[1]] + p[3]

def p_statements_empty(p):
    'statements : '
    p[0] = []

def p_stmt_if_then(p):
    'stmt : IF exp compoundstmt'
    p[0] = ("if-then", p[2], p[3])

def p_stmt_if_then_else(p):
    'stmt : IF exp compoundstmt ELSE compoundstmt'
    p[0] = ('if-then-else', p[2], p[3], p[5])

def p_stmt_assign(p):
    'stmt : IDENTIFIER EQUAL exp'
    p[0] = ('assign', p[1], p[3])

def p_stmt_return(p):
    'stmt : RETURN exp'
    p[0] = ('return', p[2])

def p_stmt_var(p):
    'stmt : VAR IDENTIFIER EQUAL exp'
    p[0] = ('var', p[2], p[4])

def p_stmt_exp(p):
    'stmt : exp'
    p[0] = ('exp', p[1])

# Here's the rules for base expressions.
def p_exp_identifier(p):
    'exp : IDENTIFIER'
    p[0] = ("identifier", p[1])

def p_exp_number(p):
    'exp : NUMBER'
    p[0] = ('number',p[1])

def p_exp_string(p):
    'exp : STRING'
    p[0] = ('string',p[1])

def p_exp_true(p):
    'exp : TRUE'
    p[0] = ('true','true')

def p_exp_false(p):
    'exp : FALSE'
    p[0] = ('false','false')

def p_exp_not(p):
    'exp : NOT exp'
    p[0] = ('not', p[2])

def p_exp_parens(p):
    'exp : LPAREN exp RPAREN'
    p[0] = p[2]

def p_exp_lambda(p):
    'exp : FUNCTION LPAREN optparams RPAREN compoundstmt'
    p[0] = ("function", p[3], p[5])

def p_binop(p):
    """ exp : exp OROR exp
            | exp ANDAND exp
            | exp EQUALEQUAL exp
            | exp LT exp
            | exp GT exp
            | exp LE exp
            | exp GE exp
            | exp PLUS exp
            | exp MINUS exp
            | exp TIMES exp
            | exp DIVIDE exp"""
    p[0] = ("binop", p[1], p[2], p[3])

def p_call(p):
    'exp : IDENTIFIER LPAREN optargs RPAREN'
    p[0] = ("call", p[1], p[3])

def p_optargs(p):
    'optargs : args'
    p[0] = p[1]

def p_optargs_empty(p):
    'optargs : '
    p[0] = []

def p_args(p):
    'args : exp COMMA args'
    p[0] = [p[1]] + p[3]

def p_args_last(p):
    'args : exp'
    p[0] = [p[1]]

#def p_error(p):
  #  print("Syntax error in input!")

jslexer = lex.lex(module=jstokens)
jsparser = yacc.yacc()

def test_parser(input_string):  # invokes your parser to get a tree!
        jslexer.input(input_string)
        parse_tree = jsparser.parse(input_string,lexer=jslexer)
        return parse_tree
