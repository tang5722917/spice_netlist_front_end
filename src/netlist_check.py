'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-07 10:47:42
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2022-09-08 16:54:39
FilePath: \spice_netlist_front_end\src\netlist_check.py
Description: Netlist input check function

Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved. 
'''
import logging
import os
import re

def checkrule(line,Debug_enable,line_num):
    checkresult=[True,'nil']

    return checkresult


def check( netlist_filename,Debug_enable ) :
    try:
        f = open(netlist_filename,'r')
        print("Open netlist "+netlist_filename+" successfully")
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
    i = 1
    netlist_list = list()
    netlist_item = list()
    for line in f.readlines():
        if i == 1:
            i = i+1
            continue
        i = i+1
        if (len(line.strip()) == 0):
            continue
        if line.strip()[0] == '*':
            continue
        if Debug_enable =='1':
            logging.info(line.strip())
        checkresult = checkrule(line,Debug_enable,i)
        if checkresult[0] == False:
            print(checkresult[1])
            os._exit(1)
        netlist_item.append(line.strip())
    netlist_list.append(netlist_item.copy())
    if Debug_enable =='1':
        logging.info("Circuit netlist End \n")
    f.close()
    return netlist_list

def pre_function( para ):
    if para == 'i' :
        return 1
    else:
        return 0
