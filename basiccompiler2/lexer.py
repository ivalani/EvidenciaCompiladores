import ply.lex as lex  
from math import pi

symbol_table = dict()

symbol_table["PI"] = pi 
symbol_table["E"] = 2.718281828459045

def myPrint(value):
    print(value)

tokens = [
    'NUMBER', 
    'VARIABLE', 
    'PLUS',
    'MINUS', 
    'TIMES', 
    'DIV', 
    'EQUAL'
    ]
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIV = r'/'
t_EQUAL = r'='

def t_NUMBER(t): 
    r'\d+\.?\d*'
    t.value = float(t.value)
    #print("Acc" , t.value)
    return t

#def t_FUNCTION(t):


def t_VARIABLE(t): 
    r'[a-zA-Z_][a-zA-z0-9_]*'
    #print("Acc" , t.value)
    return t

def t_error(t): 
    print("Error on ", t.value)
    t.lexer.skip(1)

print("Lexer v1.0")

lexer = lex.lex()
result = 0
current_op = 0
PLUS_OP = 1 
MINUS_OP = 2
TIMES_OP = 3
DIV_OP = 4 


while True: 
    data = input(">")

    if(data == 'exit'): 
        break

    if(data == 'st'): 
        print(symbol_table)
        continue
    
    lexer.input(data)
    result = 0
    current_op = 0
    last_read_var =""
    assigment = 0
    while True:
        tok = lexer.token()
        if not tok:
            print("Finish: ", result)
            if (assigment !=0):
                symbol_table[last_read_var] = result
            break

        if tok.type == 'NUMBER': 
            if current_op == 0:
                result = tok.value
            if current_op == PLUS_OP:
                result += tok.value
            if current_op == MINUS_OP: 
                result -= tok.value
            if current_op == TIMES_OP:
                result *= tok.value
            if current_op == DIV_OP:
                result /= tok.value 

        if tok.type == 'EQUAL':
            assigment = last_read_var
            
        if tok.type == 'VARIABLE':
            if assigment == 0 and current_op == 0: 
                last_read_var = tok.value

            if tok.value in symbol_table: 
                val = symbol_table[tok.value]
            else: 
                #print ("warning:symbol not found, replaced with 0")
                val =  result 

            if current_op == 0:
                result = val 
            if current_op == PLUS_OP: 
                result += val 
            if current_op == MINUS_OP:
                result -= val 
            if current_op == TIMES_OP:
                result *= val
            if current_op == DIV_OP: 
                result /= val 


        if tok.type == 'PLUS':
            current_op = PLUS_OP
        if tok.type == 'MINUS':
            current_op = MINUS_OP
        if tok.type == 'TIMES':
            current_op = TIMES_OP
        if tok.type == 'DIV':
            current_op = DIV_OP
                

print("\nended")

