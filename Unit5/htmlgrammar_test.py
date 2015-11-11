import htmlgrammar
import htmltokens

from htmltokens import tokens
import ply.lex as lex
import ply.yacc as yacc

htmllexer = lex.lex(module=htmltokens)
htmlparser = yacc.yacc(module=htmlgrammar)

def test_parser(input_string):
    htmllexer.input(input_string)
    parse_tree = htmlparser.parse(input_string,lexer=htmllexer)
    return parse_tree

f = open('37_factorial.html')
contents = f.read()
print(test_parser(contents))
