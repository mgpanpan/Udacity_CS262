import ply.lex as lex
import ply.yacc as yacc
import htmltokens
import htmlgrammar
import htmlinterp
import graphics

htmllexer = lex.lex(module=htmltokens)
htmlparser = yacc.yacc(module=htmlgrammar, tabmodule="parsetabhtml")

f = open("37_factorial.html")
contents = f.read()
parse_tree = htmlparser.parse(contents, lexer=htmllexer)

graphics.initialize()
htmlinterp.interpret(parse_tree)
graphics.finalize()


