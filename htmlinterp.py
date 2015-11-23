import ply.lex as lex
import ply.yacc as yacc
import htmltokens
import htmlgrammar
import jsinterp
import jstokens
import jsgrammar
import graphics


htmllexer = lex.lex(module=htmltokens)
htmlparser = yacc.yacc(module=htmlgrammar,tabmodule="parsetabhtml")


# Recursively Interpret an HTML AST
def interpret(ast):
    # graphics.initialize()
    for node in ast:
        nodetype = node[0]
        if nodetype == "word-element":
            graphics.word(node[1])
        elif nodetype == "tag-element":
            tagname = node[1]
            tagargs = node[2]
            subast = node[3]
            closetagname = node[4]
            if tagname != closetagname:    # this error has detected at the parse step.
                graphics.warning("(mismatched" + tagname + " " + closetagname + ")")
            else:
                graphics.begintag(tagname, tagargs)
                interpret(subast)
                graphics.endtag()
        elif nodetype == "javascript-element":
            jstext = node[1]
            jslexer = lex.lex(module=jstokens)
            jsparser = yacc.yacc(module=jsgrammar,tabmodule="parsetabjs")
            jsast = jsparser.parse(jstext,lexer=jslexer)
            result = jsinterp.jsinterp(jsast)
            htmlast = htmlparser.parse(result,lexer=htmllexer)
            interpret(htmlast)
    # graphics.finalize()
