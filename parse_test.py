import jsgrammars
import jstokens
import ply.lex as lex
import ply.yacc as yacc

jslexer = lex.lex(module=jstokens)
jsparser = yacc.yacc(module=jsgrammars)

def test_parser(input_string):  # invokes your parser to get a tree!
    jslexer.input(input_string)
    parse_tree = jsparser.parse(input_string,lexer=jslexer)
    return parse_tree

f = open("test_input/fib.js")
fib = f.read()
parse_tree = test_parser(fib)
print(parse_tree)
