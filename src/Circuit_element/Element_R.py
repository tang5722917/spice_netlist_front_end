'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-08 17:21:56
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2022-09-27 19:34:06
FilePath: \spice_netlist_front_end\src\Circuit_element\Element_R.py
Description:  Resistor model class

Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved. 
'''

from Circuit_element import Element_2port

class Element_R(Element_2port.Element_2port):
    def print_elem(self):
        return "Resistor :"+self.element_name+" Node 1->"+self.node_name_list[0]+" Node 2->"+self.node_name_list[1]

    