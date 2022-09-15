'''
Author: Donald Duck tang5722917@163.com
Date: 2022-09-12 23:35:08
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2022-09-15 19:49:21
FilePath: \spice_netlist_front_end\SNFE_test.py
Description: SNFE auto test script
Copyright (c) 2022 by Donald Duck email: tang5722917@163.com, All Rights Reserved.
'''
import time
start_time = time.time()
import sys
import os
import configparser
import logging
import platform
import argparse

sys.path.append(".")
sys.path.append("./test")

import Test_set
import Test_help

config = configparser.ConfigParser()
config.read('./test/test.cfg')
Number_test_sets = config['Test_sets']['Number_test_sets']
Default_test_set = config['Test_sets']['Default_test_set']
logging.basicConfig(filename="test_log.txt", filemode="w", format="%(message)s", datefmt="%d-%M-%Y %H:%M:%S", level=logging.DEBUG)
logging.info('Time: '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
logging.info('Number of test sets: ' + Number_test_sets )
logging.info('Input parameter: ' + str(sys.argv)+'\n' )

optparser = argparse.ArgumentParser(description='SNFE Auto test tool')
optparser.add_argument("Test_Num",nargs='?', type=int,help="Test circuit number into test set (0 - n)",
                      default=0 )
optparser.add_argument("Test_Set",nargs='?', type=int,help="Test set number (0 - n), default set can define by ",
                      default= int(Default_test_set) )
optparser.add_argument("-v", "--version", help="show the version info for the test tool",
                    action="store_true")
optparser.add_argument("--logpath", help="--logpath=<file path/name> :Modify the log path/name. (eg:--logpath='./test/log.txt')",
                        default='autotest_log.txt')
optparser.add_argument("-a","--all" ,help="Run all test circuit incuded by test.cfg " ,
                        action="store_true")

sets_list = list()
for i in range(0,int(Number_test_sets)):
    PATH_test_set = config['Test_set_'+str(i)]['PATH_test_set_'+str(i)]
    Name_test_set = config['Test_set_'+str(i)]['Name_test_set_'+str(i)]
    Info_test_set = config['Test_set_'+str(i)]['Info_test_set_'+str(i)]
    testset = Test_set.Test_set(PATH_test_set,Name_test_set,Info_test_set)
    sets_list.append(testset)

try:
    args = optparser.parse_args()
except argparse.ArgumentError:
    os._exit(1)
if args.version :
    Test_help.show_version()
    os._exit(1)
elif args.all:  # 运行全部test circuit
    print("Start all test!")
    for set in sets_list:
        cfg_name = set.cfg_is_exit()
        set.cfg_import(cfg_name)
        set.run_all_circuit()
        print('Log path :' + args.logpath)
        print("Finish all test successfully!")
        os._exit(1)

# 运行某一个circuit test
test_num = args.Test_Num
test_Set_num = args.Test_Set

print("Run the test circuit : "+ str(test_num) + " in test set : " + str(test_Set_num))
print("Test set info :" + sets_list[test_Set_num].print_test_set_info() )
cfg_name = sets_list[test_Set_num].cfg_is_exit()
sets_list[test_Set_num].cfg_import(cfg_name)
print("Test circuit info :" + sets_list[test_Set_num].print_test_circuit_info(test_num) )
sets_list[test_Set_num].run_circuit(test_num)
print('Log path :' + args.logpath)
print("Finish test successfully!")
