'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-05 15:54:09
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2022-09-13 17:06:21
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
import netlist_cal_main

logfile_name = 'log.txt'
SNFE_argv = sys.argv
for arg in SNFE_argv:
    if('--logpath=' in arg ):
        logfile_name = arg[10:]

config = configparser.ConfigParser()
config.read('SNFE.cfg')
Debug_enable = config['Debug']['Debug_enable']
if Debug_enable =='1':
    print("Debug enable")
    logging.basicConfig(filename=logfile_name, filemode="w", format="%(levelname)s:%(message)s", datefmt="%d-%M-%Y %H:%M:%S", level=logging.DEBUG)
    logging.info('Time: '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    logging.info('Input parameter: ' + str(SNFE_argv) )
else:print("Debug unable")

net_aftercheck = 0

para_list = list()
if len(SNFE_argv) == 1:
    print("No netlist/parameter input")
else :
    for i in range(1,len(SNFE_argv)):
        if (SNFE_argv[i][:2] == '--') :
            para_list.append(SNFE_argv[i][2:])
        elif SNFE_argv[i][0] == '-':
            if len (SNFE_argv[i]) !=2  :
                print("Error parameter input")
                logging.error('undefine options!')
                os._exit(1)
            para_list.append(SNFE_argv[i][1])
        else:
            netlist_filename = SNFE_argv[i]
            if Debug_enable =='1':
                logging.info('Input circuit netlist name: ' + netlist_filename  )
            #Input netlist file and first check for the netlist file
            net_aftercheck = netlist_check.check( netlist_filename,Debug_enable)
    # Pre-deal SNFE input parameter
    for i in range(0,len(para_list)):
        if(para_list[i] == 'h') :
            netlist_check.pre_function('para_list[i]')
        elif(para_list[i] == 'v') :
            netlist_check.pre_function('para_list[i]')
        elif(para_list[i] == 'help') :
            netlist_check.pre_function('para_list[i]')
        elif(para_list[i] == 'version') :
            netlist_check.pre_function('para_list[i]')
        elif('logpath=' in para_list[i] ):
            netlist_check.pre_function('para_list[i]')
        else :
            print("undefine options!")
            if Debug_enable =='1':
                logging.error('undefine options!')
            os._exit(1)
    # Deal netlist file after first check, output this circuit object(Node, Element, Model,  Control)
    if net_aftercheck != 0:
        circuit_obj = netlist_deal_main.netlist_deal_main(net_aftercheck,Debug_enable)

    #Generate run para setting for SNFE input
    para_setting = list()
    for i in range(0,len(para_list)):
        if(para_list[i] == 'h') :
            SNFE_help.print_help()
        elif(para_list[i] == 'v') :
            SNFE_help.show_version()
        elif(para_list[i] == 'help') :
            SNFE_help.print_help()
        elif(para_list[i] == 'version') :
            SNFE_help.show_version()
        if Debug_enable =='1':
            logging.info('The run parameter option: \'' + para_list[i] + '\''  )
    #Generate ocatve .m file
    if net_aftercheck != 0:
        octave_run_list = netlist_cal_main.netlist_cal_main(circuit_obj,para_setting,Debug_enable)
