'''
Author: Donald Duck tang5722917@163.com
Date: 2022-09-13 02:04:19
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2022-09-13 16:58:06
FilePath: \spice_netlist_front_end\test\Test_Circuit.py
Description:Circuit test class
Copyright (c) 2022 by Donald Duck email: tang5722917@163.com, All Rights Reserved.
'''
import logging
import os

class Test_Circuit :
    def __init__(self,circuit_name,circuit_info,circuit_setting,path_cir):
        self.circuit_name=circuit_name
        self.circuit_setting=circuit_setting
        self.circuit_info=circuit_info
        self.path_cir = path_cir
        logging.info('Test Circuit: '+self.circuit_name+' | Test setting :'+ str(self.circuit_setting) )
        logging.info('Test Info: '+self.circuit_info)

    def run_test(self):
        if self.circuit_setting == 0:
            os.system("python SNFE.py "+self.path_cir+self.circuit_name+'/'+self.circuit_name+'.cir --logpath='+self.path_cir+self.circuit_name+'/'+self.circuit_name+'_log.txt')
