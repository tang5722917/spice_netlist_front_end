'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-05 18:10:49
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2022-09-13 16:55:49
FilePath: \spice_netlist_front_end\src\SNFE_help.py
Description:  SNFE help file

Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved.
'''
def print_help() :
    print("*******************************************************************************\n")
    print("S(pice) N(etlist) F(ront) E(end) help info")
    print("SNFE.py [option] files")
    print("file  -- Circuit netlist file .sp/.SP/.cir/.CIR")
    print("[option] :\n -h/--help : show the help info for SNFE")
    print("--logpath=<file path/name> :Modify the log path/name. (eg:--logpath='./test/log.txt') ")
    print("-v/--version : show the version info for SNFE")
    print("\n*******************************************************************************")

def show_version() :
    print("*******************************************************************************\n")
    print("S(pice) N(etlist) F(ront) E(end) version info")
    print(" 0.01 ")
    print(" The soft is developping ")
    print("\n*******************************************************************************")
