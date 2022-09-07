'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-05 15:54:09
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2022-09-07 11:39:49
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
import SNFE_help
import netlist_check
import netlist_deal_main

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
    for i in range(1,len(SNFE_argv)):
        if (SNFE_argv[i][:2] == '--') :
            para_list.append(SNFE_argv[i][2:])
        elif SNFE_argv[i][0] == '-':
            para_list.append(SNFE_argv[i][1])
        else:
            netlist_filename = SNFE_argv[i]
            if Debug_enable =='1':
                logging.info('Input circuit netlist name: ' + netlist_filename  )
            fnetfile = netlist_check.check( netlist_filename,Debug_enable)

    for i in range(0,len(para_list)):
        if(para_list[i] == 'h') :
            netlist_check.pre_function('para_list[i]')
        elif(para_list[i] == 'help') :
            netlist_check.pre_function('para_list[i]')
        else : 
            print("undefine options!")
            if Debug_enable =='1':
                logging.error('undefine options!')
            os._exit(1)

    for i in range(0,len(para_list)):
        if(para_list[i] == 'h') :
            SNFE_help.print_help()
        elif(para_list[i] == 'help') :
            SNFE_help.print_help()
        if Debug_enable =='1':
            logging.info('The run parameter option: \'' + para_list[i] + '\''  )
