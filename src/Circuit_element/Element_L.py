'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-14 16:48:39
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2022-09-14 16:50:18
FilePath: \spice_netlist_front_end\src\Circuit_element\Element_L.py
Description: Inductor model class

Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved. 
'''
from Circuit_element import Element_2port

class Element_L(Element_2port.Element_2port):
    
    def print_L(self):
        print(self)