'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-08 17:14:54
LastEditors: Donald Duck tang5722917@163.com
LastEditTime: 2022-09-16 00:41:50
FilePath: /spice_netlist_front_end/src/Circuit_element/Circuit_node.py
Description: Circuit Node class
Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved.
'''
class Circuit_node:
    def __init__(self,Node_name):
       self.Node_name = Node_name
       self.elem_list = list()

    def node_append(self, Element_obj):
        self.elem_list.append( Element_obj )

    def print_node_name(self):
        return self.Node_name

    def eq_name(self,node_name):
        return (self.Node_name == node_name)
