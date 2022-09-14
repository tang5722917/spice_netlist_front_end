'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-08 17:04:39
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2022-09-14 11:54:27
FilePath: \spice_netlist_front_end\src\Circuit_element\Element.py
Description: Circuit Element base class

Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved.
'''

class Element:
    def __init__(self,element_name):
        self.element_name = element_name
        self.node_obj_list = list()
        self.model_obj_list = list()

