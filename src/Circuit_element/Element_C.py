'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-14 16:48:21
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2022-09-14 16:49:14
FilePath: \spice_netlist_front_end\src\Circuit_element\Element_C.py
Description: capacitor model class

Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved. 
'''
from Circuit_element import Element_2port

class Element_C(Element_2port.Element_2port):
    
    def print_C(self):
        print(self)