'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-07 10:47:42
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2022-09-07 11:56:30
FilePath: \spice_netlist_front_end\src\netlist_check.py
Description: Netlist input check function

Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved. 
'''
import logging
import os
import re

def check( netlist_filename,Debug_enable ) :
    try:
        f = open(netlist_filename,'r')
        print("Open netlist "+netlist_filename+"successfully")
    except OSError as reason:
        print('Error :'+ str(reason))
        if Debug_enable =='1':
            logging.error('Error :'+ str(reason))
        os._exit(1)
    finally:
        if f in locals():
            f.close()
    if Debug_enable =='1':
        logging.info("Circuit Netlist\n")
    for line in f.readlines():
        if (len(line.strip()) == 0):
            continue
        if line.strip()[0] == '*':
            continue
        if Debug_enable =='1':
            logging.info(line.strip())
    if Debug_enable =='1':
        logging.info("Circuit netlist End \n")
    return f

def pre_function( para ):
    if para == 'i' :
        return 1
    else:
        return 0
