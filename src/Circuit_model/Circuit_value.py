'''
Author: Donald Duck tang5722917@163.com
Date: 2022-09-17 10:52:35
LastEditors: Donald Duck tang5722917@163.com
LastEditTime: 2022-09-17 11:05:13
FilePath: /spice_netlist_front_end/src/Circuit_model/Circuit_value.py
Description:
Copyright (c) 2022 by Donald Duck email: tang5722917@163.com, All Rights Reserved.
'''
import os
class Circuit_value:
    def __init__(self,str):
        if type(str).__name__ == 'str':
            self.__postfix_unit_handling(str)
        else:
            print("Error netlist input! ")
            os._exit(1)

    def __postfix_unit_handling(self, value_str):
        i = 0
        while i < len(value_str[0]):
            print(value_str[0][-1*(i+1)])
            i += 1
