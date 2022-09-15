'''
Author: Donald Duck tang5722917@163.com
Date: 2022-09-16 03:13:14
LastEditors: Donald Duck tang5722917@163.com
LastEditTime: 2022-09-16 03:40:57
FilePath: /spice_netlist_front_end/src/Circuit/Circuit_print_info.py
Description: Print the circuit info
Copyright (c) 2022 by Donald Duck email: tang5722917@163.com, All Rights Reserved.
'''
from Circuit import Circuit_operator

class Circuit_print_info (Circuit_operator.Circuit_operator):
    def log_element_info(self):
        self.logging.info("\n*****************************************************")
        self.logging.info("            Circuit Element Statistics               ")
        self.logging.info("*****************************************************\n")
    def log_node_info(self):
        self.logging.info("\n*****************************************************")
        self.logging.info("               Circuit Node Statistics                 ")
        self.logging.info("*****************************************************\n")
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
