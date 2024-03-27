'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-14 10:40:41
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2024-03-27 20:22:19
FilePath: \spice_netlist_front_end\src\Circuit\circuit_element_fac.py
Description:

Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved.
'''
from Circuit_element import Element_R
from Circuit_element import Element_V
from Circuit_element import Element_I
from Circuit_control import Control_fac
from Net_syntax import Netlist_lex

class Circuit_element_fac :
    def __init__(self):
        self.type = {
            "VSource_net_element"   : self.get_VSource_net_element,
            "R_net_element"         : self.get_R_net_element,
            "CONTROL"               : self.get_Control_element,
            "Comment"               : self.get_Comment,
        }
        self.control_fac = Control_fac.Control_fac()
        
     #V source obj
    def get_VSource_net_element(self,line_ob): 
        obj = Element_V.Element_V(line_ob.toks[0].value)
        obj.import_elem(line_ob)
        return [obj,0]
    #Resistor obj    
    def get_R_net_element(self,line_ob):
        obj = Element_R.Element_R(line_ob.toks[0].value)
        obj.import_elem(line_ob)
        return [obj,0]
    #Control obj    
    def get_Control_element(self,line_ob):
        return self.control_fac.import_elem(line_ob)
    
    def get_Comment(self,line_ob):
        return [-1,-1]
    
    def netlist_element_deal(self,net_line,lineno):
        line_ob = Netlist_lex.get_net_line_ob(net_line,lineno)
    # result [obj,statue]
    # statue 0 : Element obj , 1 : Control obj , 2 : Model obj , 0 < error
        func = self.type.get(line_ob.toks[0].type)
        if func:
            return func(line_ob)
        else:
            return [-3,-3]
