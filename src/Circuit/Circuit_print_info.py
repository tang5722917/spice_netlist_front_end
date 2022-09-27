'''
Author: Donald Duck tang5722917@163.com
Date: 2022-09-16 03:13:14
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2022-09-27 19:45:26
FilePath: \spice_netlist_front_end\src\Circuit\Circuit_print_info.py
Description: Print the circuit info
Copyright (c) 2022 by Donald Duck email: tang5722917@163.com, All Rights Reserved.
'''
from Circuit import Circuit_operator

class Circuit_print_info (Circuit_operator.Circuit_operator):
    def log_element_info(self):
        self.logging.info("\n*****************************************************")
        self.logging.info("            Circuit Element Statistics               ")
        self.logging.info("*****************************************************\n")
        for elem in self.elem_obj_list:
            self.logging.info(elem.print_elem())
    def log_node_info(self):
        self.logging.info("\n*****************************************************")
        self.logging.info("               Circuit Node Statistics                 ")
        self.logging.info("*****************************************************\n")
        for node in self.node_obj_list:
            self.logging.info(node.print_node())
    def log_model_info(self):
        self.logging.info("\n*****************************************************")
        self.logging.info("              Circuit Model Statistics                 ")
        self.logging.info("*****************************************************\n")
    def log_simulation_info(self):
        self.logging.info("\n*****************************************************")
        self.logging.info("              Circuit Simulation Statistics            ")
        self.logging.info("*****************************************************\n")
    def log_all_info(self):
        self.log_element_info()
        self.log_node_info()
        self.log_model_info()
        self.log_simulation_info()
