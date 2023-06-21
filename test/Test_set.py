'''
Author: Donald Duck tang5722917@163.com
Date: 2022-09-13 01:05:58
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2023-06-21 15:17:41
FilePath: \spice_netlist_front_end\test\Test_set.py
Description:Test set class
Copyright (c) 2022 by Donald Duck email: tang5722917@163.com, All Rights Reserved.
'''
import os
import sys
import logging
import configparser

from Test_Circuit import Test_Circuit


class Test_set:

    def __init__(self,set_path,set_name,set_info,test_config):
        self.set_path=set_path
        self.set_name=set_name
        self.set_info=set_info
        self.test_config = test_config
        self.Number_test_circuit = 0
        logging.info('Circuit test set '+set_name +' PATH: '+set_path)
        logging.info(self.set_info + '\n')
        self.circuit_list = list()


    def cfg_is_exit(self):
        cfg_filename = self.set_path + self.set_name + '_test.cfg'
        try:
            f = open(cfg_filename,'r')
        except OSError as reason:
            print('Error :'+ str(reason))
            os._exit(1)
        finally:
            if f in locals():
                f.close()
        logging.info("Open test cfg file: "+cfg_filename+" successfully")
        f.close()
        return cfg_filename

    def cfg_import(self,cfg_name):
        config = configparser.ConfigParser()
        config.read(cfg_name)
        self.Number_test_circuit = int(config['Test_circuit']['Number_test_circuit'])
        logging.info('Circuit test set '+ self.set_name +' includes '+str(self.Number_test_circuit) + ' test circuits.')
        for i in range(0,self.Number_test_circuit):
            Name_test_cir = config['Test_cir_'+str(i)]['Name_test_circuit_'+str(i)]
            Info_test_cir = config['Test_cir_'+str(i)]['Info_test_circuit_'+str(i)]
            testcir = Test_Circuit(Name_test_cir,Info_test_cir,self.test_config,self.set_path)
            self.circuit_list.append(testcir)

    def run_all_circuit(self) :
        if len(self.circuit_list) != 0:
            for cir in self.circuit_list:
                cir.run_test()
                
    def run_circuit(self,num):
        logging.info("Test set info :" + self.print_test_set_info())
        self.circuit_list[num].run_test()

    def print_test_set_info(self):
        return self.set_info

    def print_test_circuit_info(self,num):
        if (num >= self.Number_test_circuit) or (num < 0) :
            print("Error test circuit number")
            os._exit(1)
        else:
            return self.circuit_list[num].print_info()
