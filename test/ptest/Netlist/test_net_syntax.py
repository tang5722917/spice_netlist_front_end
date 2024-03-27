'''
Author: Donald duck tang5722917@163.com
Date: 2024-03-25 20:51:01
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2024-03-26 17:40:18
Description: 
Copyright (c) 2024 by Donald duck email: tang5722917@163.com, All Rights Reserved.
'''
import Net_test
from Net_syntax import Netlist_lex

class Test_net_syntax:
    def test_R_net_element_1(self):
        data = 'R1 gnd vcc 10K'
        data_1 = ["R1","gnd","vcc",'10K']
        toks = Netlist_lex.net_syntax(data)
        Net_test.net_element_RLC_assert(toks,data_1)
        data = 'r100 100 0 4.7k'
        toks = Netlist_lex.net_syntax(data)
        data_2 = ["r100",100,0,"4.7k"]
        Net_test.net_element_RLC_assert(toks,data_2)
        data = 'Rr Rr 0 0.1Ohm'
        toks = Netlist_lex.net_syntax(data)
        data_3 = ["Rr","Rr",0,"0.1Ohm"]
        Net_test.net_element_RLC_assert(toks,data_3)


    def test_V_net_element_1(self):
        data = 'V1 gnd vcc 10V'
        data_1 = ["V1","gnd","vcc",'10V']
        toks = Netlist_lex.net_syntax(data)
        Net_test.net_element_VI_assert(toks,data_1)
