'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-14 16:51:01
LastEditors: Donald Duck tang5722917@163.com
LastEditTime: 2022-09-16 00:14:45
FilePath: /spice_netlist_front_end/src/Circuit_element/Element_I.py
Description: Current source model class

Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved.
'''
from Circuit_element import Element_source

class Element_I(Element_source.Element_source):

    def print_I(self):
        print(self)
