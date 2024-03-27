'''
Author: Donald duck tang5722917@163.com
Date: 2024-03-26 20:32:21
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2024-03-27 19:23:45
Description: 
Copyright (c) 2024 by Donald duck email: tang5722917@163.com, All Rights Reserved.
'''
Control_type = {
    '.endc'  : 'endc',
    '.end'   : 'end',
    '.op'    : 'op',
    '.dc'    : 'dc'
}


def control_lookup(value) :
    type = Control_type.get(value.lower())
    return type
