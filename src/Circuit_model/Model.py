'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-16 11:26:42
LastEditors: Donald Duck tang5722917@163.com
LastEditTime: 2022-09-17 11:54:18
FilePath: /spice_netlist_front_end/src/Circuit_model/Model.py
Description:  Model base class
            Value postfix and unit handling
Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved.
'''
import re

class Model:
    def __init__(self,model_name):
        self.model_name = model_name
