def hash_get_func(key,redisConnect):
    pass

def hash_set_func(command):
    pass

def hash_mget_func(command):
    pass

def hash_mset_func(command):
    pass

def hash_del_func(command):
    pass

dic_string_commandswitch = {"hash_getcommand":hash_get_func,
                            "hash_setcommand":hash_set_func,
                            "hash_mgetscommand":hash_mget_func,
                            "hash_msetcommand": hash_mset_func,
                            "hash_delcommand":hash_del_func}

def hash_func(command):
    '''
    运行hash命令
    :return:
    '''
    print('hash_func')