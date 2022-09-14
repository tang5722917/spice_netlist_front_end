'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-07 10:48:28
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2022-09-14 17:34:07
FilePath: \spice_netlist_front_end\src\netlist_deal_main.py
Description: Deal the netlsit
             Covert the netlist to circuit object
Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved. 
'''
from Circuit import Circuit


def netlist_deal_main(net_aftercheck,Debug_enable) :
    circuit_obj_list = list()
    circuit_num = 0
    for netlist in net_aftercheck:
        cir = Circuit(str(circuit_num),Debug_enable)
        circuit_num = circuit_num + 1
        s = cir.import_circuit_elem(netlist)
        if s != False:
            for i in s :
                print(i)
        circuit_obj_list.append(cir)
    return circuit_obj_list
    