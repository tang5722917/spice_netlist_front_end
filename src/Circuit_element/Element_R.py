'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-08 17:21:56
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2022-09-08 17:39:05
FilePath: \spice_netlist_front_end\src\Circuit_element\Element_R.py
Description: 

Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved. 
'''
from Circuit_element import Element

class Element_R(Element.Element):
    def __init__(self,element_name):
        self.element_name = element_name