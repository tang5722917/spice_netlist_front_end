'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-08 17:04:39
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2022-09-16 17:14:26
FilePath: \spice_netlist_front_end\src\Circuit_element\Element.py
Description: Circuit Element base class

Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved.
'''

class Element:
    def __init__(self,element_name):
        self.element_name = element_name
        self.node_obj_list = list()
        self.model_obj_list = list()
        self.node_name_list = list()

    def node_append(self,node):
        self.node_obj_list.append(node)
    
    def model_append(self,model):
        self.model_obj_list.append(model)
