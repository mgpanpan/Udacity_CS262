import htmltokens
import ply.lex as lex

f = open('37_factorial.html')
contents = f.read()
# print(contents)

lexer = lex.lex(module=htmltokens)
def alltokens(input_string):
    lexer.input(input_string)
    result = [ ]
    while True:
         tok = lexer.token()
         if not tok: break
         result = result + [(tok.type, tok.value)]
    return result

print(alltokens(contents))

d = {'a': 1, 'c': 3}

print(dict(d.items()))
