'''
Author: Donald duck tang5722917@163.com
Date: 2022-09-08 17:14:54
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2022-09-08 17:20:54
FilePath: \spice_netlist_front_end\src\Circuit_element\Node.py
Description: Node name class

Copyright (c) 2022 by Donald duck tang5722917@163.com, All Rights Reserved. 
'''
class Node:
    Node_name = ''
    Node_connect = list()
    def __init__(self,Node_name) :
       self.Node_name = Node_name

    def Node_append(self, Element_obj):
        self.Node_connect.append( Element_obj )