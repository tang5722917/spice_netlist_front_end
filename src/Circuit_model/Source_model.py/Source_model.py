'''
Author: Donald Duck tang5722917@163.com
Date: 2022-09-18 01:07:31
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2022-09-27 19:37:47
FilePath: \spice_netlist_front_end\src\Circuit_model\Source_model.py\Source_model.py
Description: Source model base class
Copyright (c) 2022 by Donald Duck email: tang5722917@163.com, All Rights Reserved.
'''
import abc

#######################################
#   Output Signal (DC/AC) base  model
#######################################

class Signal_model:
    @abc.abstractclassmethod
    def signal_output(self):pass

###############################
#   Source base  model
###############################

class Source_model:
    def __init__(self) :
        self.signal = list()

    def add_signal_pattern(self,signal_pattern) :
            self.signal.append(signal_pattern)

    @abc.abstractclassmethod
    def signal_pattern_output(self):pass


class Source_V_model(Source_model):
    def signal_pattern_output(self):
        pass


class Source_I_model(Source_model):
    def signal_pattern_output(self):
        pass
