'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-08 17:21:56
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2022-09-14 16:49:44
FilePath: \spice_netlist_front_end\src\Circuit_element\Element_R.py
Description:  Resistor model class

Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved. 
'''

from Circuit_element import Element_2port

class Element_R(Element_2port.Element_2port):
    
    def print_R(self):
        print(self)

    