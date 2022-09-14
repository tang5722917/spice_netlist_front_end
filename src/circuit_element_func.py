'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-14 10:40:41
LastEditors: Donald Duck tang5722917@163.com
LastEditTime: 2022-09-14 20:48:36
FilePath: /spice_netlist_front_end/src/circuit_element_func.py
Description:

Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved.
'''
from Circuit_element import Element_R
from Circuit_element import Element_V

from Circuit_Control import Control_op

def netlist_element_deal(net_line,statue_net):
    elem = net_line.split()
    # result [obj,statue]
    # statue 0 : Element obj , 1 : Control obj , 2 : Model obj , 0 < error
    if statue_net == 0:
        if elem[0][0] == 'v' or  elem[0][0] == 'V':       #DC source
            obj = Element_V.Element_V(elem[0])
            obj.import_elem(elem[1],elem[2],elem[3:])
            obj.printV()
            return [obj,0]
        elif elem[0][0] == 'r' or  elem[0][0] == 'R':       #Resistor
            obj = Element_R.Element_R(elem[0])
            obj.import_elem(elem[1],elem[2],elem[3:])
            obj.print_R()
            return [obj,0]
        elif elem[0].lower() == '.op':
            if len(elem) > 1:
                obj = Control_op.Control_op( elem[2:] )
            else:
                obj = Control_op.Control_op()
            obj.print_op()
            return [obj,1]
        elif elem[0].lower() == '.control':       #Control deck
            statue_net = 1
        elif elem[0].lower() == '.endc':       #Control deck end
            statue_net = 0
        elif elem[0].lower() == '.end':       #Netlist end
            statue_net = 0
        else:
            return [-1,-1]
        return [-2,-2]
