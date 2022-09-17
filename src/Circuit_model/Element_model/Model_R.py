'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-16 17:58:39
LastEditors: Donald Duck tang5722917@163.com
LastEditTime: 2022-09-18 00:55:33
FilePath: /spice_netlist_front_end/src/Circuit_model/Element_model/Model_R.py
Description:  Resistor class

Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved.
'''
from Circuit_model import Model

class Model_R(Model.Model):
    def __init__(self, value):
        self.value = value
