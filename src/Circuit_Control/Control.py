'''
Author: Donald Duck tang5722917@163.com
Date: 2022-09-14 20:18:37
LastEditors: Donald Duck tang5722917@163.com
LastEditTime: 2022-09-15 06:54:59
FilePath: /spice_netlist_front_end/src/Circuit_Control/Control.py
Description:Control base class
Copyright (c) 2022 by Donald Duck email: tang5722917@163.com, All Rights Reserved.
'''
class Control:
    Control_statue = 0     #Netlist statue para
# 0  input net connection and .* deck
# 1  input control deck
# -1 Finish netlist input
    def __init__(self,control_para = []):
        self.control_para = control_para

class Control_start(Control):
    def __init__(self):
        Control.control_para = 0

class Control_end(Control):
    def __init__(self):
        Control.control_para = -1

class Control_endc(Control):
    def __init__(self):
        Control.control_para = 0

class Control_control(Control):
    def __init__(self):
        Control.control_para = 1
