'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-08 16:09:02
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2024-03-27 19:21:07
Description: 
Copyright (c) 2024 by Donald duck email: tang5722917@163.com, All Rights Reserved.
'''

import ply.lex as lex
from Net_syntax import Netlist_tokens
from Net_syntax import Netlist_control_tokens

#List of token name
tokens = [
    'NUMBER',
    'FLOAT_NUM',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'Comment',
    'R_net_element',
    'L_net_element',
    'C_net_element',
    'VSource_net_element',
    'ISource_net_element',
    "CONTROL",
    'ID']

#Regular expression rule for simple tokens
# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'


def t_R_net_element(t) :
    r'^[rR][0-9a-zA-Z-_]+'
    return t

def t_L_net_element(t) :
    r'^[Ll][0-9a-zA-Z-_]+'
    return t

def t_C_net_element(t) :
    r'^[Cc][0-9a-zA-Z-_]+'
    return t

def t_VSource_net_element(t):
    r'^[Vv][0-9a-zA-Z-_]+'
    return t

def t_ISource_net_element(t):
    r'^[Ii][0-9a-zA-Z-_]+'
    return t

# A regular expression rule with some action code

def t_FLOAT_NUM(t):
    r'[-+]?([0-9]*\.[0-9]+|[0-9]+\.)((?i)meg|ohm|[kmgunpvah]?)'
    return t

def t_NUMBER(t):
    r'[-+]?[0-9]+((?i)meg|ohm|[kmgunpvah]?)'
    return t
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_CONTROL(t):
    r'\.[a-zA-Z_][a-zA-Z_0-9]*'
    # Look up symbol table information and return a tuple
    t.value = (t.value, Netlist_control_tokens.control_lookup(t.value))
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

def t_Comment(t):
    r'[\#\*].*'
    t.value = str(t.value)  
    return t
    # No return value. Token discarded

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
def net_syntax(data):
    # Build the lexer
    lexer = lex.lex()
    # Give the lexer some input
    lexer.input(data)
    # Tokenize
    toks = list()
    for tok in lexer:
        toks.append(tok)
    return toks

def get_net_line_ob(data,lineno):
    toks = net_syntax(data)
    netline_ob = Netlist_tokens.Netlist_Tokens(toks,lineno)
    return netline_ob
