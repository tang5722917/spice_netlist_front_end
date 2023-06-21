'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-14 11:44:46
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2023-06-21 15:27:59
FilePath: \spice_netlist_front_end\src\Circuit_element\Element_I.py
Description: Volt Source class

Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved.
'''
from Circuit_element import Element_source


class Element_I(Element_source.Element_source):
    def print_elem(self):
        return 'Current Source :' + self.element_name+" Node 1->"+self.node_name_list[0]+":  Node 2->"+self.node_name_list[1]
