'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-16 11:26:42
LastEditors: Donald Duck tang5722917@163.com
LastEditTime: 2022-09-17 11:02:32
FilePath: /spice_netlist_front_end/src/Circuit_model/Model.py
Description:  Model base class
            Value postfix and unit handling
Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved.
'''
import re

class Model:
    def __init__(self,model_name):
        self.model_name = model_name
#Unit
# Current -- A
# Voltage -- V
# Resistance -- Ohm/O
# Inductance -- H
# Capacitance -- C
# Frequence -- Hz
# Time -- s
# Power -- W

# postfix
#    p       n      u       m     1    k      meg      g       t
# 10e-12   10e-9   10e-6  10e-3   1   10e3   10e-6    10e9    10e12
