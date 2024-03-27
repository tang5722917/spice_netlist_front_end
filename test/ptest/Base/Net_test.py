'''
Author: Donald duck tang5722917@163.com
Date: 2024-03-26 13:59:23
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2024-03-27 19:24:28
Description: 
Copyright (c) 2024 by Donald duck email: tang5722917@163.com, All Rights Reserved.
'''

def net_element_RLC_assert(toks,data):
        assert len(toks) >= 4 
        assert toks[0].type in ["R_net_element","L_net_element","C_net_element"]
        assert toks[0].value == data[0]
        assert toks[1].type in ["NUMBER","ID"]
        assert toks[1].value == str(data[1])
        assert toks[2].type in ["NUMBER","ID"]
        assert toks[2].value == str(data[2])
        assert toks[3].type in ["NUMBER","FLOAT_NUM"]
        assert toks[3].value == data[3]

def net_element_VI_assert(toks,data):
        assert len(toks) >= 4 
        assert toks[0].type in ['VSource_net_element','ISource_net_element']
        assert toks[0].value == data[0]
        assert toks[1].type in ["NUMBER","ID"]
        assert toks[1].value == str(data[1])
        assert toks[2].type in ["NUMBER","ID"]
        assert toks[2].value == str(data[2])
        assert toks[3].type in ["NUMBER","FLOAT_NUM"]
        assert toks[3].value == data[3]

def net_element_control_assert(toks,data):
        assert len(toks) >= 1
        assert toks[0].type == "CONTROL"
        assert toks[0].value[1] == data[0]
