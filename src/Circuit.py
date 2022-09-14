'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-14 09:47:16
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2022-09-14 14:17:38
FilePath: \spice_netlist_front_end\src\Circuit.py
Description: 

Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved. 
'''
from sqlalchemy import false
import circuit_element_func as cef

class Circuit :
    Circuit_num = 0

    def __init__(self,circuit_name,Debug_enable):
        self.circuit_name = circuit_name
        self.Debug_enable = Debug_enable
        Circuit.Circuit_num += 1
        self.elem_obj_list = list()
        self.node_obj_list = list()
        self.model_obj_list = list()
        self.control_obj_list = list()


    def import_circuit_elem(self,netlist):
        statue_net = 0
    #statue_net    0/1
    #0 : default , circuit netlist deck
    #1 : Control statue, between '.control' and '.endc'
        for net_line in netlist:
            obj = cef.netlist_element_deal(net_line,statue_net)
            if obj[1] == 0:
                self.elem_obj_list.append(obj[0])
            elif obj[1] == 1:
                self.control_obj_list.append(obj[0])
            elif obj[1] == 2:
                self.model_obj_list.append(obj[0])
            else :
                return false
        return [len(self.elem_obj_list),len(self.control_obj_list),len(self.model_obj_list)]
    



