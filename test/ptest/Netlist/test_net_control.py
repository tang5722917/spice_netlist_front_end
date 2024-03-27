'''
Author: Donald duck tang5722917@163.com
Date: 2024-03-27 19:09:37
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2024-03-27 19:16:45
Description: 
Copyright (c) 2024 by Donald duck email: tang5722917@163.com, All Rights Reserved.
'''
import Net_test
from Net_syntax import Netlist_lex

class Test_net_control:
    def test_net_control_1(self):
        data = '.end'
        data_1 = ["end"]
        toks = Netlist_lex.net_syntax(data)
        Net_test.net_element_control_assert(toks,data_1)
