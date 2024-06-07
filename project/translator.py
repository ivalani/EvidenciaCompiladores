import ply.lex as lex
import ply.yacc as yacc

from math import pi
from math import pow
from library import *

import networkx as nx
import matplotlib.pyplot as plt

parseGraph = None
NODE_COUNTER = 0

def add_node(attr):
    global parseGraph
    global NODE_COUNTER

    attr["counter"] = NODE_COUNTER
    parseGraph.add_node(NODE_COUNTER, **attr)
    NODE_COUNTER += 1
    return parseGraph.nodes[NODE_COUNTER-1]

symbol_table = dict()

symbol_table["PI"] = pi
symbol_table["E"] = 2.718281828459045

def myPrint(v1, v2, v3, v4):
    print("Printing: ", v1, v2, v3, v4)

def do_nothing():
    print("Doing nothing")

def sumAB(a,b):
    return a+b

symbol_table["myPrint"] = myPrint
symbol_table["do_nothing"] = do_nothing
symbol_table["sumAB"] = sumAB
symbol_table["load"] = load_image
symbol_table["show"] = show_image


tokens = (
    'NUMBER',
    'VARIABLE',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIV',
    'EQUAL',
    'EXP',
    'LPAREN',
    'RPAREN',
    'COMMA',
    'CONNECT',
    'STRING'
    )

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIV = r'/'
t_EQUAL = r'='
t_EXP = r'\^'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_CONNECT = r'->'

def t_STRING(t):
    r'\"(.)*\"'
    t.value = t.value[1:-1]

    return t

def t_NUMBER(t):
    r'\d+\.?\d*'
    t.value = float(t.value)
    return t

def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_error(t):
    print("Error on  ", t.value)
    t.lexer.skip(1)

print("Translator v1.0")

lexer = lex.lex()

def p_assignment_assign(p):
    """
    assignment : VARIABLE EQUAL expression
    """
    node = add_node({"type": "ASSIGN", "label": f'=', "value": ''})
    node_var = add_node({"type": "VARIABLE_ASSIGN", "label": f'VAR_{p[1]}', "value": p[1]})

    parseGraph.add_edge(node["counter"], node_var["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

def p_assignment_flow(p):
    """
    assignment : VARIABLE EQUAL flow
    """
    node = add_node( {"type": 'ASSIGN', "label": f'=', "value": ''} )
    node_var = add_node( {"type": "VARIABLE_ASSIGN", "label": f'VAR_{p[1]}', "value": p[1]} )
    parseGraph.add_edge(node["counter"], node_var["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

def p_flow(p):
    """
    flow : VARIABLE CONNECT flow_functions
    """
    connections = parseGraph.neighbors(p[3][0]["counter"])

    for c in connections:
        # El nodo con el ID c
        c = parseGraph.nodes[c]

        if ( c["type"] == "PENDING_NODE"):
            c["type"] = "VARIABLE"
            c["label"] = f"VAR_{p[1]}"
            c["vale"] = p[1]
            break

    p[0] = p[3][-1]
def p_flow_functions(p):
    """
    flow_functions : flow_function_call CONNECT flow_functions
    """

    # Dime los vecinos del ID del nodo qué estpa ahi
    connections = parseGraph.neighbors(p[3][0]["counter"])

    for c in connections:
        # El nodo con el ID c
        c = parseGraph.nodes[c]

        if ( c["type"] == "PENDING_NODE"):
            parseGraph.add_edge(  c["counter"], p[1]["counter"] )
            break

    p[0] = [p[1]] + p[3]

def p_flow_functions_alone(p):
    """
    flow_functions : flow_function_call
    """
    p[0] = [p[1]]

def p_flow_function_call(p):
    """
    flow_function_call : VARIABLE LPAREN params RPAREN
    """
    pass

    node = add_node({"type": "FLOW_FUNCTION_CALL", "label": f"ff_{p[1]}", "value":p[1]})
    pending_node = add_node({"type": "PENDING_NODE", "label": f"pending", 'value': '' })
    parseGraph.add_edge(node["counter"], pending_node["counter"])

    for n in p[3]:
        parseGraph.add_edge(node["counter"], n["counter"])

    p[0] = node


def p_assignment_expression(p):
    """
    assignment : expression
    """
    p[0] = p[1]

def p_expression_plus(p):
    """
    expression : expression PLUS term
    """
    node = add_node({"type": "PLUS", "label": f'+', "value": ''})
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

def p_expression_minus(p):
    """
    expression : expression MINUS term
    """
    node = add_node({"type": "MINUS", "label": f'-', "value": ''})
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

def p_expression_term(p):
    """
    expression : term
                | string_def
    """
    p[0] = p[1]

def p_string_def(p):
    """
    string_def : STRING
    """
    p[0] = add_node({'type': "STRING", 'label': p[1], 'value': p[1]})

def p_term_exponent(p):
    """
    term : exponent
    """
    p[0] = p[1]

def p_term_times(p):
    """
    term : term TIMES exponent
    """
    node = add_node({"type": "TIMES", "label": f'*', "value": ''})
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

def p_term_div(p):
    """
    term : term DIV exponent
    """
    node = add_node({"type": "DIV", "label": f'/', "value": ''})
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

def p_exponent_factor(p):
    """
    exponent : factor
    """
    p[0] = p[1]

def p_exponent_exp(p):
    """
    exponent : factor EXP factor
    """
    node = add_node({"type": "POWER", "label": f'POW', "value": ''})
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

def p_factor_number(p):
    """
    factor : NUMBER
    """
    n = add_node({"type": "NUMBER", "label": f'NUM_{p[1]}', "value": p[1]})
    p[0] = n

def p_factor_variable(p):
    """
    factor : VARIABLE
    """
    p[0] = add_node({"type": "VARIABLE", "label": f'VAR_{p[1]}', "value": p[1]})

def p_factor_expression(p):
    """
    factor : LPAREN expression RPAREN
    """
    node = add_node({"type": "GROUP", "label": f'( )', "value": ''})
    parseGraph.add_edge(node["counter"], p[2]["counter"])
    p[0] = node

def p_factor_function_call(p):
    """
    factor : function_call
    """
    p[0] = p[1]

def p_function_call_no_params(p):
    """
    function_call : VARIABLE LPAREN RPAREN
    """
    p[0] = add_node({"type": "FUNCTION_CALL", "label": f'FUNC_{p[1]}', "value": p[1]})

def p_function_call_with_params(p):
    """
    function_call : VARIABLE LPAREN params RPAREN
    """
    node = add_node({"type": "FUNCTION_CALL", "label": f'FUNC_{p[1]}', "value": p[1]})
    for n in p[3]:
        parseGraph.add_edge(node["counter"], n["counter"])
    p[0] = node

def p_params_multiple(p):
    """
    params : params COMMA expression
    """
    p[0] = p[1] + [p[3]]

def p_params_single(p):
    """
    params : expression
    """
    p[0] = [p[1]]

def p_error(p):
    print("Syntax error in input: ", p)

def execute_parse_tree(tree):
    root = tree.nodes
    root_id = 0
    res = visit_node(tree, root_id, -1)
    return res

def visit_node(tree, node_id, from_id):
    children = tree.neighbors(node_id)
    res = []
    for c in children:
        if c != from_id:
            res.append(visit_node(tree, c, node_id))
    current_node = tree.nodes[node_id]

    if current_node["type"] == "INITIAL":
        return res[0]

    if current_node["type"] == "ASSIGN":
        symbol_table[res[0]] = res[1]
        return res[1]

    if current_node["type"] == "NUMBER":
        return current_node["value"]

    if current_node["type"] == "STRING":
        return current_node["value"]

    if current_node["type"] == "PENDING_NODE":
        return res[0]

    if current_node["type"] == "VARIABLE_ASSIGN":
        return current_node["value"]

    if current_node["type"] == "VARIABLE":
        if current_node["value"] in symbol_table:
            return symbol_table[current_node["value"]]
        print("ERROR! Variable not found, returning 0")
        return 0

    if (current_node["type"] == "FUNCTION_CALL" or current_node["type"] == "FLOW_FUNCTION_CALL"):
        if current_node["value"] in symbol_table:
            if len(res) > 0:
                return symbol_table[current_node["value"]](*res)
            else:
                return symbol_table[current_node["value"]]()
        print("ERROR! Function not found, returning 0")
        return 0

    if current_node["type"] == "POWER":
        return pow(res[0], res[1])

    if current_node["type"] == "PLUS":
        return res[0] + res[1]

    if current_node["type"] == "MINUS":
        return res[0] - res[1]

    if current_node["type"] == "TIMES":
        return res[0] * res[1]

    if current_node["type"] == "DIV":
        return res[0] / res[1]

    if current_node["type"] == "GROUP":
        return res[0]

parser = yacc.yacc()

result = 0
current_op = 0

while True:
    data = input(">")

    if data == 'exit':
        break

    if data == 'st':
        print(symbol_table)
        continue

    parseGraph = nx.Graph()
    NODE_COUNTER = 0
    root = add_node({"type": "INITIAL", "label": "INIT"})

    result = parser.parse(data)

    if result:
        parseGraph.add_edge(root["counter"], result["counter"])
        labels = nx.get_node_attributes(parseGraph, 'label')
        nx.draw(parseGraph, labels=labels, with_labels=True)
        plt.show()
        result = execute_parse_tree(parseGraph)
        print("Result: ", result)
    else:
        print("Failed to parse input.")

print("\nended")