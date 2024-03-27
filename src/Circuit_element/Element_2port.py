'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-14 11:47:08
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2024-03-26 20:23:18
FilePath: \spice_netlist_front_end\src\Circuit_element\Element_2port.py
Description: Two port element base class

Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved.
'''
from Circuit_element import Element

class Element_2port(Element.Element):
    def import_elem(self,line_ob):
        self.node_name_list.append(line_ob.toks[1].value)
        self.node_name_list.append(line_ob.toks[2].value)
        self.model_name = line_ob.toks[3].value

    def return_pos_node(self):
        return self.node_obj_list[0]

    def return_neg_node(self):
        return self.node_obj_list[1]

    def return_model_name(self):
        return self.model_name
