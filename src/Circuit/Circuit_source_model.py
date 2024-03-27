'''
Author: Donald Duck tang5722917@163.com
Date: 2022-09-17 13:42:24
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2024-03-26 20:00:45
FilePath: \spice_netlist_front_end\src\Circuit\Circuit_source_model.py
Description:Source Model operate class
Copyright (c) 2022 by Donald Duck email: tang5722917@163.com, All Rights Reserved.
'''
from Circuit import Circuit_operator
from Circuit_model import Model
from Circuit_model import Circuit_value

class Circuit_source_model(Circuit_operator.Circuit_operator):
    def init_circuit_model(self):
        for elem in self.elem_obj_list:
            if ((type(elem).__name__) == 'Element_V') or ((type(elem).__name__) == 'Element_I') \
                    or ((type(elem).__name__) == 'Element_C'):
                obj = Model.Model('Value')
                Circuit_value.Circuit_value(elem.return_model_name()[1],self.logging)
