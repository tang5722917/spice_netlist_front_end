'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-14 11:44:46
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2022-09-14 16:52:11
FilePath: \spice_netlist_front_end\src\Circuit_element\Element_V.py
Description: Volt Source class 

Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved. 
'''
from Circuit_element import Element_2port


class Element_V(Element_2port.Element_2port):
    def printV(self):
        print(self)