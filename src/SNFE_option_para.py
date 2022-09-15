'''
Author: Donald Duck tang5722917@163.com
Date: 2022-09-16 01:42:03
LastEditors: Donald Duck tang5722917@163.com
LastEditTime: 2022-09-16 01:51:56
FilePath: /spice_netlist_front_end/src/SNFE_option_para.py
Description:
Copyright (c) 2022 by Donald Duck email: tang5722917@163.com, All Rights Reserved.
'''
class SNFE_option_para:
    # 0 : default, only import netlist and export the octave .m file
    # 1 : Import netlist and do simulation using SPICE_OctSolver
    SNFE_output_action = 0
    def set_SNFE_output_action(self,num):
        SNFE_option_para.SNFE_output_action = num
    def get_SNFE_output_action(self):
        return SNFE_option_para.SNFE_output_action
