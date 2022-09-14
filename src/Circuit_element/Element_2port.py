'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-14 11:47:08
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2022-09-14 14:06:57
FilePath: \spice_netlist_front_end\src\Circuit_element\Element_2port.py
Description: 

Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved. 
'''
from Circuit_element import Element

class Element_2port(Element.Element):
    def import_elem(self,node_name1,node_name2,model_name):
        self.node_name1 = node_name1
        self.node_name2 = node_name2
        self.model_name = model_name
    
    