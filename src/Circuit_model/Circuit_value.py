'''
Author: Donald Duck tang5722917@163.com
Date: 2022-09-17 10:52:35
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2022-09-27 19:16:55
FilePath: \spice_netlist_front_end\src\Circuit_model\Circuit_value.py
Description:
Copyright (c) 2022 by Donald Duck email: tang5722917@163.com, All Rights Reserved.
'''
import os
import sys
from decimal import Decimal

class Circuit_value:
    def __init__(self,str,logging):
        self.logging = logging
        if type(str).__name__ == 'str':
            value = self.postfix_unit_handling(str)
            if value != False:
                self.value = value
            else:
                print("Error netlist input! ")
                self.logging.info("Error netlist input! \n Maybe there is error value number in netlist")
                os._exit(1)
        else:
            print("Error netlist input! ")
            self.logging.info("Error netlist input! \n Maybe there is error value string in netlist")
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
        try :
            float_num = eval(temp[1])
        except OSError as err:
            print("OS error: {0}".format(err))
            return False
        if (type(float_num).__name__ != 'float') & (type(float_num).__name__ != 'int'):
            print("Illrgal number in netlist !")
            return False
        value_property.append(float_num*value_property[1])
        print(value_property[0],value_property[1],value_property[2])

##########################################################################

    def postfix_scale_handling(self,value_str):
        i = 0
        value_scale = 1
        while i < len(value_str):
            value_str = value_str.lower()
            s = value_str[-1*(i+1)]
            if(s == 'k') :
                value_scale = 1000.0
            elif ('meg' in value_str ):
                value_scale = 1000000.0
                return [value_scale,value_str[:-1*(i+3)] ]
            elif(s == 'g') :
                value_scale = 1000000000.0
            elif(s == 't') :
                value_scale = 1000000000000.0
            elif(s == 'm') :
                value_scale = 0.001
            elif(s == 'u') :
                value_scale = 0.000001
            elif(s == 'n') :
                value_scale = 0.000000001
            elif(s == 'p') :
                value_scale = 0.000000000001
            else:
                return [value_scale,value_str]
            return [value_scale,value_str[:-1*(i+1)] ]


    def unit_handling(self, value_str):
        i = 0
        value_type = "none"
        value_str = value_str.lower()
        s = value_str[-1*(i+1)]
        if((s == 'o') ):
            value_type = 'type_R'
        elif (s == 'v'):
            value_type = 'type_V'
        elif (s == 'a'):
            value_type = 'type_I'
        elif('ohm' in value_str ):
            value_type = 'type_R'
            return [value_type,value_str[:-1*(i+3)] ]
        else:
            return [value_type,value_str]
        return [value_type,value_str[:-1*(i+1)] ]
