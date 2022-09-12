'''
Author: Donald Duck tang5722917@163.com
Date: 2022-09-12 23:35:08
LastEditors: Donald Duck tang5722917@163.com
LastEditTime: 2022-09-13 02:54:35
FilePath: /spice_netlist_front_end/SNFE_test.py
Description: SNFE auto test script
Copyright (c) 2022 by Donald Duck email: tang5722917@163.com, All Rights Reserved.
'''
import sys
import os
import configparser
import logging
import time

sys.path.append(".")
sys.path.append("./test")

import Test_set

SNFE_test_argv = sys.argv
print("Start test!")

config = configparser.ConfigParser()
config.read('./test/test.cfg')
Number_test_sets = config['Test_sets']['Number_test_sets']

logging.basicConfig(filename="test_log.txt", filemode="w", format="%(levelname)s:%(message)s", datefmt="%d-%M-%Y %H:%M:%S", level=logging.DEBUG)
logging.info('Time: '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
logging.info('Number of test sets: ' + Number_test_sets )
logging.info('Input parameter: ' + str(SNFE_test_argv)+'\n' )

sets_list = list()
for i in range(0,int(Number_test_sets)):
    PATH_test_set = config['Test_set_'+str(i)]['PATH_test_set_'+str(i)]
    Name_test_set = config['Test_set_'+str(i)]['Name_test_set_'+str(i)]
    Info_test_set = config['Test_set_'+str(i)]['Info_test_set_'+str(i)]
    testset = Test_set.Test_set(PATH_test_set,Name_test_set,Info_test_set)
    sets_list.append(testset)

for set in sets_list:
    cfg_name = set.cfg_is_exit()
    set.cfg_import(cfg_name)
    set.run_all_circuit()

print("Finish test successfully!")
