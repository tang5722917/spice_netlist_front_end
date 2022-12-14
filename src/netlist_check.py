'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-07 10:47:42
LastEditors: Donald Duck tang5722917@163.com
LastEditTime: 2022-09-16 03:25:40
FilePath: /spice_netlist_front_end/src/netlist_check.py
Description: Netlist input check function

Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved.
'''
import os
import re

def checkrule(line,Debug_enable,line_num):
    checkresult=[True,'nil']

    return checkresult


def check( netlist_filename,Debug_enable,logging,option_para) :
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
        logging.info("Circuit Netlist")
        logging.info("********************************************")
    i = 1
    netlist_list = list()
    netlist_item = list()
    for line in f.readlines():
        if i == 1:
            i = i+1
            logging.info("Circuit title : " + line)
        i = i+1
        if ((Debug_enable =='1') & (len(line.strip()) != 0)) :
            if ((line.strip())[0] !='*'):
                logging.info(line.strip())
        checkresult = checkrule(line,Debug_enable,i)
        if checkresult[0] == False:
            print(checkresult[1])
            os._exit(1)
        netlist_item.append(line.strip())
    netlist_list.append(netlist_item.copy())
    if Debug_enable =='1':
        logging.info("********************************************")
        logging.info("Circuit netlist End \n")
    f.close()
    return netlist_list

def pre_function( para ):
    if para == 'i' :
        return 1
    else:
        return 0
