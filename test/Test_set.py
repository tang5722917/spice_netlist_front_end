'''
Author: Donald Duck tang5722917@163.com
Date: 2022-09-13 01:05:58
LastEditors: Donald Duck tang5722917@163.com
LastEditTime: 2022-09-13 02:53:52
FilePath: /spice_netlist_front_end/test/Test_set.py
Description:Test set class
Copyright (c) 2022 by Donald Duck email: tang5722917@163.com, All Rights Reserved.
'''
import os
import sys
import logging
import configparser

from Test_Circuit import Test_Circuit


class Test_set:
    circuit_list = list()

    def __init__(self,set_path,set_name,set_info):
        self.set_path=set_path
        self.set_name=set_name
        self.set_info=set_info
        logging.info('Circuit test set '+set_name +' PATH: '+set_path)
        logging.info(self.set_info + '\n')


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
        # 0 : default, only import netlist and export the octave .m file
        test_setting = 0
        config = configparser.ConfigParser()
        config.read(cfg_name)
        Number_test_circuit = int(config['Test_circuit']['Number_test_circuit'])
        logging.info('Circuit test set '+ self.set_name +' includes '+str(Number_test_circuit) + ' test circuits.')
        logging.info('Test circuit setting : ')
        logging.info('                      0 : default, only import netlist and export the octave .m file \n')
        for i in range(0,Number_test_circuit):
            Name_test_cir = config['Test_cir_'+str(i)]['Name_test_circuit_'+str(i)]
            Info_test_cir = config['Test_cir_'+str(i)]['Info_test_circuit_'+str(i)]
            testcir = Test_Circuit(Name_test_cir,Info_test_cir,test_setting,self.set_path)
            self.circuit_list.append(testcir)

    def run_all_circuit(self) :
        if len(self.circuit_list) != 0:
            for cir in self.circuit_list:
                cir.run_test()
