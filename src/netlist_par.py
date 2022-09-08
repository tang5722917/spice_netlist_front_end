'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-08 16:09:02
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2022-09-08 16:09:22
FilePath: \spice_netlist_front_end\src\netlist_par.py
Description: 

Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved. 
'''
import ply.lex as lex
import ply.yacc as yacc


def netlist_par_deal(Debug_enable):
    #List of token name
    tokens = (
        'Comment'
        'R_net_element',
        'L_net_element',
        'C_net_element',
        'VSource_net_element',
        'Node_value_element',
    )
    #Regular expression rule for simple tokens
    t_Comment = r'^\*[*]+'
    t_R_net_element = r'^R[0-9a-zA-Z-_]+'
    t_L_net_element = r'^L[0-9a-zA-Z-_]+'
    t_C_net_element = r'^C[0-9a-zA-Z-_]+'
    t_VSource_net_element = r'^V[0-9a-zA-Z-_]+'
    t_Node_value_element = r'[0-9a-zA-Z-_]+'
    t_ignore = ' \t'

    data = "*Vsource 1 0 10"
    lexer =lex.lex()
    lexer.input(data)
    while True :
        tok = lexer.token()
        if not tok:break
        print (tok.type,tok.value,tok.lineno, tok.lexpos)
    return 1