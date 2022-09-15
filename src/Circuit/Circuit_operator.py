'''
Author: Donald Duck tang5722917@163.com
Date: 2022-09-16 03:27:17
LastEditors: Donald Duck tang5722917@163.com
LastEditTime: 2022-09-16 03:36:41
FilePath: /spice_netlist_front_end/src/Circuit/Circuit_operator.py
Description:Circuit operator base class
Copyright (c) 2022 by Donald Duck email: tang5722917@163.com, All Rights Reserved.
'''
from Circuit import Circuit

class Circuit_operator(Circuit.Circuit):
    def __init__(self,cir) :
        self.Circuit_num=cir.Circuit_num
        self.circuit_name = cir.circuit_name
        self.elem_obj_list = cir.elem_obj_list
        self.node_obj_list = cir.node_obj_list
        self.model_obj_list = cir.model_obj_list
        self.control_obj_list = cir.control_obj_list
        self.option_para=cir.option_para
        self.logging = cir.logging
        self.Debug_enable = cir.Debug_enable
