'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-05 15:54:09
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2022-09-05 17:41:43
FilePath: \spice_netlist_front_end\SNFE.py
Description: Spice Netlist Front End
             Startup python 

Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved. 
'''
import sys 
import os
import time
import re
import configparser
import logging

sys.path.append("./src")
SNFE_argv = sys.argv

config = configparser.ConfigParser()
config.read('SNFE.cfg')
Debug_enable = config['Debug']['Debug_enable']
if Debug_enable =='1':
    print("Debug enable")
    logging.basicConfig(filename="log.txt", filemode="w", format="%(levelname)s:%(message)s", datefmt="%d-%M-%Y %H:%M:%S", level=logging.DEBUG)
    logging.info('Time: '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    logging.info('Input parameter: ' + str(SNFE_argv) )
else:print("Debug unable")

para_list = list()
if len(SNFE_argv) == 1:
    print("No netlist/parameter input")
else :
    for i in range(0,len(SNFE_argv)-1):
        if (SNFE_argv[i-1][:2] == '--') :
            para_list.append(SNFE_argv[i-1][2:])
        elif SNFE_argv[i-1][0] == '-':
            para_list.append(SNFE_argv[i-1][1])
        else:
            circuit_file_name = SNFE_argv[i-1]
            