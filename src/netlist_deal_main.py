'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-07 10:48:28
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2022-09-13 17:44:48
FilePath: \spice_netlist_front_end\src\netlist_deal_main.py
Description: Deal the netlsit
             Covert the netlist to circuit object
Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved. 
'''
import string
from Circuit_element import Element_R 
''' 
    statue_net    0/1
    0 : default , circuit netlist deck
    1 : Control statue, between '.control' and '.endc'
'''
def netlist_element_deal(net_line,Elements_list,Node_list):
    statue_net = 0
    elem = net_line.split()
    if elem[0][0] == 'v' or  elem[0][0] == 'V':       #DC source
        print(elem)
    elif elem[0][0] == 'r' or  elem[0][0] == 'R':       #Resistor
        print(elem)
    elif elem[0].lower() == '.op':      
        print(elem)
    elif elem[0].lower() == '.control':       #Control deck
        statue_net = 1
    elif elem[0].lower() == '.endc':       #Control deck end
        statue_net = 0
    return 1


def netlist_deal_main(netlist_list, Debug_enable) : 
    for netlist in netlist_list:
        Elements_list = list()
        Node_list = list()
        for net_line in netlist:
            netlist_element_deal(net_line,Elements_list,Node_list)
    return 1
    