'''
Author: Donald Duck tang5722917@163.com
Date: 2022-09-17 10:52:35
LastEditors: Donald Duck tang5722917@163.com
LastEditTime: 2022-09-17 14:49:15
FilePath: /spice_netlist_front_end/src/Circuit_model/Circuit_value.py
Description:
Copyright (c) 2022 by Donald Duck email: tang5722917@163.com, All Rights Reserved.
'''
import os
from decimal import Decimal

class Circuit_value:
    def __init__(self,str):
        if type(str).__name__ == 'str':
            self.postfix_unit_handling(str)

        else:
            print("Error netlist input! ")
            os._exit(1)
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

    def postfix_unit_handling(self,str):
        value_property = list()
        temp = self.unit_handling(str)
        value_property.append(temp[0])
        temp = self.postfix_scale_handling(temp[1])
        value_property.append(temp[0])
        value_property.append = Decimal(temp[1])
        print(value_property[0],value_property[1],value_property[2])

##########################################################################

    def postfix_scale_handling(self,value_str):
        i = 0
        value_scale = 1
        while i < len(value_str):
            value_str = value_str.lower()
            s = value_str[-1*(i+1)]
            if(s == 'k') :
                value_scale = 1000
            elif ('meg' in value_str ):
                value_scale = 1000000
                return [value_scale,value_str[:-1*(i+3)] ]
            else:
                return [value_scale,value_str]
            return [value_scale,value_str[:-1*(i+1)] ]

        print(value_scale)

    def unit_handling(self, value_str):
        i = 0
        value_type = "none"
        value_str = value_str.lower()
        s = value_str[-1*(i+1)]
        if((s == 'o') ):
            value_type = 'type_R'
        elif (s == 'v'):
            value_type = 'type_V'
        elif('ohm' in value_str ):
            value_type = 'type_R'
            return [value_type,value_str[:-1*(i+3)] ]
        else:
            return [value_type,value_str]
        return [value_type,value_str[:-1*(i+1)] ]
