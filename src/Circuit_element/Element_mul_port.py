'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-14 17:01:33
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2022-09-14 17:02:03
FilePath: \spice_netlist_front_end\src\Circuit_element\Element_mul_port.py
Description: Multiple port element base class

Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved. 
'''
from Circuit_element import Element

class Element_mul_port(Element.Element):
    def import_elem(self,node_name,model_name):
        self.node_name = node_name
        self.model_name = model_name