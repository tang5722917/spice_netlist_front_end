'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-14 11:47:08
LastEditors: Donald Duck tang5722917@163.com
LastEditTime: 2022-09-16 00:30:32
FilePath: /spice_netlist_front_end/src/Circuit_element/Element_2port.py
Description: Two port element base class

Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved.
'''
from Circuit_element import Element

class Element_2port(Element.Element):
    def import_elem(self,node_name1,node_name2,model_name):
        self.node_name_list.append(node_name1)
        self.node_name_list.append(node_name2)
        self.model_name = model_name

    def return_pos_node(self):
        return self.node_obj_list[0]

    def return_neg_node(self):
        return self.node_obj_list[1]
