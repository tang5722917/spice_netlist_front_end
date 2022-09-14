'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-14 16:51:01
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2022-09-14 16:51:18
FilePath: \spice_netlist_front_end\src\Circuit_element\Element_I.py
Description: Current source model class

Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved. 
'''
from Circuit_element import Element_2port

class Element_I(Element_2port.Element_2port):
    
    def print_I(self):
        print(self)