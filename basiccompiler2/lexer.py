import ply.lex as lex  

tokens = [
    'NUMBER', 
    'VARIABLE'
]

def t_NUMBER(t): 
    r'\d+'
    print("Acc" , t.value)
    return t

def t_VARIABLE(t): 
    r'[a-zA-Z_][a-zA-z0-9_]*'
    print("Acc" , t.value)
    return t

def t_error(t): 
    print("Error on ", t.value)
    t.lexer.skip(1)

print("Lexer v1.0")

lexer = lex.lex()
data = input(">")
lexer.input(data)

tok = lexer.token()

print("\nended")
