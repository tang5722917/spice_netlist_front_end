'''
Author: Donald duck tang5722917@163.com
Date: 2024-03-25 13:01:20
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2024-03-26 20:20:18
Description: 
Copyright (c) 2024 by Donald duck email: tang5722917@163.com, All Rights Reserved.
'''

class Netlist_Tokens:
    def __init__(self,toks,lineno):
        self.toks = toks.copy()
        self.len = len(toks)
        self.type = toks[0].type
        self.lineno = lineno
        
    
        
    
