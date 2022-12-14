'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-05 15:54:09
LastEditors: Donald Duck tang5722917@163.com
LastEditTime: 2022-09-16 03:25:21
FilePath: /spice_netlist_front_end/SNFE.py
Description: Spice Netlist Front End
             Startup python

Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved.
'''
import time
start_time = time.time()
import sys
sys.path.append("./src")
import os
import platform
import argparse
import SNFE_help
import netlist_check
import netlist_deal_main
import netlist_cal_main
import SNFE_option_para
import configparser
import logging

option_para = SNFE_option_para.SNFE_option_para()
optparser = argparse.ArgumentParser(description='S(pice) N(etlist) F(ront) E(end) help info')
optparser.add_argument("-v", "--version", help="show the version info for SNFE",
                    action="store_true")
optparser.add_argument("--logpath", help="--logpath=<file path/name> :Modify the log path/name. (eg:--logpath='./test/log.txt')",
                        default='log.txt')
optparser.add_argument("Netlist_file",nargs='?', type=str,help="Circuit file name (.cir/.sp/.ckt)",
                      default='none' )
optparser.add_argument("-o","--octsolver" ,help="Import netlist and do simulation using SPICE_OctSolver" ,
                        action="store_true")

try:
    args = optparser.parse_args()
except argparse.ArgumentError:
    os._exit(1)
if args.version :
    SNFE_help.show_version()
    os._exit(1)
elif args.octsolver:
    option_para.set_SNFE_output_action(1)  # -o / -octsolver
print('Log path :' + args.logpath)

config = configparser.ConfigParser()
config.read('SNFE.cfg')
Debug_enable = config['Debug']['Debug_enable']
print("Debug enable")
logging.basicConfig(filename=args.logpath, filemode="w", format="%(message)s", datefmt="%d-%M-%Y %H:%M:%S", level=logging.DEBUG)
logging.info('Time: '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
logging.info("********************************************************************************")
logging.info("CPU info : "+ platform.processor())
logging.info("OS info : "+ platform.system() + platform.release() )
logging.info("Python info : "+ platform.python_version() )

logging.info("********************************************************************************")
logging.info('\nInput parameter: ' + str(sys.argv) )


net_aftercheck = 0


logging.info('\nInput circuit netlist name: ' + args.Netlist_file  )
if args.Netlist_file != 'none':
#Input netlist file and first check for the netlist file
    net_aftercheck = netlist_check.check( args.Netlist_file,Debug_enable,logging,option_para)
    # Pre-deal SNFE input parameter

    # Deal netlist file after first check, output this circuit object(Node, Element, Model,  Control)
    if net_aftercheck != 0:
        circuit_obj = netlist_deal_main.netlist_deal_main(net_aftercheck,Debug_enable,logging,option_para)

    #Generate run para setting for SNFE input
    para_setting = list()

    #Generate ocatve .m file
    if net_aftercheck != 0:
        octave_run_list = netlist_cal_main.netlist_cal_main(circuit_obj,option_para,Debug_enable,logging,option_para)
else:
    logging.info('\nError!\nPlease input correct netlist file name'  )
    print('\nError!\nPlease input correct netlist file name')
end_time = end = time.time()
print ("SNFE run time : "+ "{:.5f}".format(end_time-start_time) + 's')
logging.info("SNFE run time : "+ "{:.5f}".format(end_time-start_time) + 's')
