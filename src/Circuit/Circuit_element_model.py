'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-16 17:52:57
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2022-09-16 18:02:32
FilePath: \spice_netlist_front_end\src\Circuit\Circuit_element_model.py
Description: Element Model operate class

Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved. 
'''
from Circuit import Circuit_operator

from Circuit_model import Model
from Circuit_model.Element_model import Model_R

class Circuit_element_model(Circuit_operator.Circuit_operator):
    def init_circuit_model(self):
        for elem in self.elem_obj_list:
            if ((type(elem).__name__) == 'Element_R') or ((type(elem).__name__) == 'Element_C') or ((type(elem).__name__) == 'Element_L'):
                obj = Model.Model('Value')
                obj.postfix_unit_handling(elem.return_model_name())