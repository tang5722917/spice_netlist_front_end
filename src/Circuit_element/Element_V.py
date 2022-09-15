'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-14 11:44:46
LastEditors: Donald Duck tang5722917@163.com
LastEditTime: 2022-09-16 00:15:16
FilePath: /spice_netlist_front_end/src/Circuit_element/Element_V.py
Description: Volt Source class

Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved.
'''
from Circuit_element import Element_source


class Element_V(Element_source.Element_source):
    def printV(self):
        print(self)
