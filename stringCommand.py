def string_get_func(key):
    pass

def string_set_func(key,value):
    pass

def string_mget_func(L_key):
    pass

def string_mset_func(L_key,L_value):
    pass

dic_string_commandswitch = {"string_getcommand":string_get_func,
                            "string_setcommand":string_set_func,
                            "key_mgetscommand":string_mget_func,
                            "string_msetcommand": string_mset_func}

def string_func(command):
    '''
    运行string命令
    :return:
    '''
    print('string_func')