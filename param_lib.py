#!/usr/bin/python3

import logger as log
import logging

def init_variables(dict_name,tc_param,srv_hdl):


    log_var = log.(logging.DEBUG,tc_param["user"],tc_param["uuid"],tc_param["cur_time"],srv_hdl,dict_name)
    test_name = dict_name
    dict_name = {}
    dict_name["testname"] = test_name
    dict_name["uuid"] = tc_param["uuid"]
    dict_name["user"] = tc_param["user"]
    dict_name["stime"] = tc_param["start_time"]
    dict_name["cur_time"] = tc_param["cur_time"]
    return dict_name,log_var
