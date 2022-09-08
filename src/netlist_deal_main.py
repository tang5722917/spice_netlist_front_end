'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-07 10:48:28
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2022-09-08 17:44:01
FilePath: \spice_netlist_front_end\src\netlist_deal_main.py
Description: 

Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved. 
'''
import sys
from Circuit_element import Element_R 


def netlist_element_deal(net_line,Elements_list,Node_list):
    element_obj = Element_R.Element_R("R1")
    return element_obj

def netlist_deal_main(netlist_list, Debug_enable) : 
    for netlist in netlist_list:
        Elements_list = list()
        Node_list = list()
        for net_line in netlist:
            netlist_element_deal(net_line,Elements_list,Node_list)
    return 1
    