'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-14 09:47:16
LastEditors: Donald Duck tang5722917@163.com
LastEditTime: 2022-09-16 03:20:30
FilePath: /spice_netlist_front_end/src/Circuit_operator/Circuit.py
Description: Circuit base class
            Building the Circuit obj
Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved.
'''
import os
import circuit_element_func as cef

from Circuit_element import Circuit_node
from Circuit_Control import Control

class Circuit :
    Circuit_num = 0

    def __init__(self,circuit_name,Debug_enable,logging,option_para):
        self.Circuit_num=Circuit.Circuit_num
        self.circuit_name = circuit_name
        self.Debug_enable = Debug_enable
        Circuit.Circuit_num += 1
        self.elem_obj_list = list()
        self.node_obj_list = list()
        self.model_obj_list = list()
        self.control_obj_list = list()
        self.option_para=option_para
        obj = Circuit_node.Circuit_node('0')
        self.node_obj_list.append(obj)
        self.logging = logging
        Control.Control_start()


    def import_circuit_elem(self,netlist):
        net_line_num = 0
    #statue_net    0/1
    #0 : default , circuit netlist deck
    #1 : Control statue, between '.control' and '.endc'
        for net_line in netlist:
            net_line_num += 1
            if (len(net_line.strip()) == 0):
                continue
            if net_line.strip()[0] == '*':
                continue
            obj = cef.netlist_element_deal(net_line)
            if obj[1] == 0:
                self.elem_obj_list.append(obj[0])
            elif obj[1] == 1:
                self.control_obj_list.append(obj[0])
            elif obj[1] == 2:
                self.model_obj_list.append(obj[0])
            elif obj[1] == -1:
                break
            else:
                self.logging.info("Import netlist error: \nCircuit:"+str(self.Circuit_num)+"\nError Line number :" + str(net_line_num) )
                print("Import netlist error: \nCircuit:"+str(self.Circuit_num)+"\nError Line number :" + str(net_line_num) )
                if obj[1] == -3:
                    print("Error reason : " + "Illegal netlist line !")
                    self.logging.info("Error reason : " + "Illegal netlist line !")
                else:
                    self.logging.info("Error reason : Maybe miss \".end\" ")
                    print("Error reason : Maybe miss \".end\" ")
                os._exit(1)
        if (Control.Control.Control_statue == -1):
            self.logging.info("Successfully import netlist :"+str(self.Circuit_num) )
        else :
            self.logging.info("Import netlist error:"+str(self.Circuit_num) )
            self.logging.info(" Error reason : Maybe miss \".end\" ")
            os._exit(1)
        return [len(self.elem_obj_list),len(self.control_obj_list),len(self.model_obj_list)]

    def Debug_logging_import_netlist(self,logging) :
        for elem in self.elem_obj_list:
            logging.info(str(elem))
        for elem in self.control_obj_list:
            logging.info(str(elem))
        for elem in self.model_obj_list:
            logging.info(str(elem))
    def _is_node_name_in_node_list(self,node_name):
        for node_obj in self.node_obj_list:
            if node_obj.eq_name(node_name):
                return node_obj
            else :
                continue
        return False

    def _add_node_list(self,node_obj,elem_obj):
        node_obj.node_append(elem_obj)
        self.node_obj_list.append(node_obj)

    def init_circuit_node(self):
        for elem in self.elem_obj_list:
            for node_name in elem.node_name_list:
                node = self._is_node_name_in_node_list(node_name)
                if node == False:
                    self._add_node_list(Circuit_node.Circuit_node(node_name),elem)
                else:
                    node.node_append(elem)
        if self.Debug_enable == '1':
            for node in self.node_obj_list:
                self.logging.info( str(node) + "  Node Name :" +node.print_node_name())
        return len(self.node_obj_list)
