'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-14 17:01:21
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2022-09-14 17:03:28
FilePath: \spice_netlist_front_end\src\Circuit_element\Element_3port.py
Description: Three port element base class

Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved. 
'''
from Circuit_element import Element

class Element_3port(Element.Element):
    def import_elem(self,node_name1,node_name2,node_name3,model_name):
        self.node_name1 = node_name1
        self.node_name2 = node_name2
        self.node_name3 = node_name3
        self.model_name = model_name