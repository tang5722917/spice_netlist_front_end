'''
Author: Donald duck tang5722917@163.com
Date: 2024-03-27 19:58:13
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2024-03-27 20:41:20
FilePath: \spice_netlist_front_end\src\Circuit_control\Control_fac.py
Description: 
Copyright (c) 2024 by Donald duck email: tang5722917@163.com, All Rights Reserved.
'''
from Circuit_control import Control_op
from Circuit_control import Control


class Control_fac :
    def __init__(self):
        self.type = {
            "op"           : self.get_end_control,
            "dc  "         : self.get_end_control,
            "end"          : self.get_end_control,
            "endc"         : self.get_endc_control,
        }
        
    def get_op_control(self,line_ob):
        if (Control.Control._is_start_status()):
            obj = Control_op.Control_op(line_ob.lineno)
        return [obj,1]
    
    def get_end_control(self,line_ob):
        if (Control.Control._is_start_status()):
            obj = Control.Control_end()
        return [0,1]
    
    def get_endc_control(self,line_ob):
        obj = Control.Control_endc()
        return [0,1]
    
    def import_elem(self,line_ob):
        print(line_ob.toks[0].value[1])
        func = self.type.get(line_ob.toks[0].value[1])
        if func:
            return func(line_ob)
        else:
            return [-3,-3]
