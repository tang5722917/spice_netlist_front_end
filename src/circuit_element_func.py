'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-14 10:40:41
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2022-09-15 16:38:29
FilePath: \spice_netlist_front_end\src\circuit_element_func.py
Description:

Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved.
'''
from Circuit_element import Element_R
from Circuit_element import Element_V

from Circuit_Control import Control_op
from Circuit_Control import Control

def netlist_element_deal(net_line):
    elem = net_line.split()
    # result [obj,statue]
    # statue 0 : Element obj , 1 : Control obj , 2 : Model obj , 0 < error
    if Control.Control.Control_statue == 0:
        if elem[0][0] == 'v' or  elem[0][0] == 'V':       #DC source
            obj = Element_V.Element_V(elem[0])
            obj.import_elem(elem[1],elem[2],elem[3:])
            return [obj,0]
        elif elem[0][0] == 'r' or  elem[0][0] == 'R':       #Resistor
            obj = Element_R.Element_R(elem[0])
            obj.import_elem(elem[1],elem[2],elem[3:])
            return [obj,0]
        elif elem[0].lower() == '.op':
            obj = Control_op.Control_op(elem)
            return [obj,1]
        elif elem[0].lower() == '.control':       #Control deck
            obj = Control.Control_control()
            return [obj,1]
        elif elem[0].lower() == '.end':       #Netlist end
            obj = Control.Control_end()
            return [obj,1]
    elif Control.Control.Control_statue == 1:
        if elem[0].lower() == '.endc':       #Control deck end
            obj = Control.Control_endc()
            return [obj,1]
        else:
            obj = Control.Ngspice_control(elem)
            return [obj,1]
    elif Control.Control.Control_statue == -1:
        print("Netlist End")
        return [-1,-1]
    else :
        print(str(elem))
    return [-2,-2]
