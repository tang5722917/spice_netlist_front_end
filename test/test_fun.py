'''
Author: Donald duck tang5722917@163.com
Date: 2023-06-21 14:56:01
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2023-06-21 15:17:54
FilePath: \spice_netlist_front_end\test\test_fun.py
Description: 一些python 函数
Copyright (c) 2023 by Donald duck email: tang5722917@163.com, All Rights Reserved.
'''

import os

def run_all_test(sets_list,args):
    print("Start all test!")
    for set in sets_list:
        cfg_name = set.cfg_is_exit()
        set.cfg_import(cfg_name)
        set.run_all_circuit()
    print('Log path :' + args.logpath)
    print("Finish all test successfully!")
    os._exit(1)
