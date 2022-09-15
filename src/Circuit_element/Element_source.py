'''
Author: Donald Duck tang5722917@163.com
Date: 2022-09-16 00:09:08
LastEditors: Donald Duck tang5722917@163.com
LastEditTime: 2022-09-16 00:33:04
FilePath: /spice_netlist_front_end/src/Circuit_element/Element_source.py
Description:Volt/Curent Source base
Copyright (c) 2022 by Donald Duck email: tang5722917@163.com, All Rights Reserved.
'''
from Circuit_element import Element_2port

class Element_source(Element_2port.Element_2port):
    def print_source(self):
        print(str(self))
