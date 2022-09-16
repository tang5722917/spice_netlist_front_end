'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-07 10:48:28
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2022-09-16 17:56:34
FilePath: \spice_netlist_front_end\src\netlist_deal_main.py
Description: Deal the netlsit
             Covert the netlist to circuit object
Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved.
'''
from Circuit import Circuit
from Circuit import Circuit_print_info
from Circuit import Circuit_element_model
def netlist_deal_main(net_aftercheck,Debug_enable,logging,option_para) :
    circuit_obj_list = list()
    circuit_num = 0
    for netlist in net_aftercheck:
        # Circuit 初始化
        cir = Circuit.Circuit(str(circuit_num),Debug_enable,logging,option_para)
        circuit_num = circuit_num + 1

        #导入netlist
        s = cir.import_circuit_elem(netlist)

        if Debug_enable == '1':
            cir.Debug_logging_import_netlist(logging)
        logging.info("The number of connections :" + str(s[0]))
        logging.info("The number of controls :" + str(s[1]))
        logging.info("The number of models :" + str(s[2]))

        #初始化电路连接，建立Node
        node_num = cir.init_circuit_node()
        if node_num > 1:
            logging.info("The number of node :" + str(node_num) )
        else :
            logging.info("Error !\nInfo : Maybe there is no connection in netlist")
        #初始化Model
        cir = Circuit_element_model.Circuit_element_model(cir)
        cir.init_circuit_model()

        cir = Circuit_print_info.Circuit_print_info(cir)
        cir.log_all_info()
        circuit_obj_list.append(cir)
    return circuit_obj_list
