'''
Author: Donald duck tang5722917@163.com
Date: 2024-03-26 19:39:17
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2024-03-26 19:45:24
Description: 
Copyright (c) 2024 by Donald duck email: tang5722917@163.com, All Rights Reserved.
'''
import Net_test
from Net_syntax import Netlist_lex

class Test_net_ob:
    def test_net_element_1(self):
        data = 'R1 gnd vcc 10K'
        data_1 = ["R1","gnd","vcc",'10K']
        line_ob = Netlist_lex.get_net_line_ob(data,1)
        assert line_ob.type == "R_net_element"
        assert line_ob.toks[1].value == "gnd"
        assert line_ob.toks[2].value == "vcc"
