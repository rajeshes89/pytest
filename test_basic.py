import param_lib
def test_iperf_tcp(srv_hdl,tc_param):
    dict_name = inspect.stack()[0][3]
    dict_param,log = param_lib.init_variables(dict_name,tc_param,srv_hdl)

    #test class call here
    
