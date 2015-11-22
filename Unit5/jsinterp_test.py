import ply.lex as lex
import ply.yacc as yacc
import jstokens
import jsgrammars
import jsinterp

jslexer = lex.lex(module=jstokens)
jsparser = yacc.yacc(module=jsgrammars)

f = open("fib.js")
contents = f.read()
parse_tree = jsparser.parse(contents, lexer=jslexer)
print(parse_tree)

print(jsinterp.jsinterp(parse_tree))

## python dictionary test
# env = {"a" : 1}
# print(env)
# env["b"] = 2
# print(env)
#
# a = (1, "a", "b")
# print(a)
# print(a + tuple("c"))

