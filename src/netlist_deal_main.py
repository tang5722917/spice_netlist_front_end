'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-07 10:48:28
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2022-09-15 17:12:16
FilePath: \spice_netlist_front_end\src\netlist_deal_main.py
Description: Deal the netlsit
             Covert the netlist to circuit object
Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved. 
'''
from Circuit import Circuit


def netlist_deal_main(net_aftercheck,Debug_enable,logging) :
    circuit_obj_list = list()
    circuit_num = 0
    for netlist in net_aftercheck:
        # Circuit 初始化
        cir = Circuit(str(circuit_num),Debug_enable,logging)
        circuit_num = circuit_num + 1
        
        #导入netlist
        s = cir.import_circuit_elem(netlist)
        
        if Debug_enable == '1':
            cir.Debug_logging_import_netlist(logging)
        logging.info("The number of connections :" + str(s[0]))
        logging.info("The number of controls :" + str(s[1]))
        logging.info("The number of models :" + str(s[2]))
        
        #初始化电路连接，建立Node
        node_num = cir.init_circuit_node(logging)
        if node_num > 1:
            logging.info("The number of node :" + str(node_num) )
        else :
            logging.info("Error !\nInfo : Maybe there is no connection in netlist")
        
        circuit_obj_list.append(cir)
    return circuit_obj_list
    