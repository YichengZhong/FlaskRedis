def key_del_func(key,redisConnect):
    result =redisConnect.delete(key)
    return result

def key_scan_func(command):
    pass

def key_exists_func(key,redisConnect):
    result = redisConnect.exists(key)
    return result

dic_key_commandswitch = {"key_delcommand":key_del_func,
                         "key_scancommand":key_scan_func,
                         "key_existscommand":key_exists_func}

def key_func(command):
    '''
    运行key命令
    :return:
    '''
    print('key_func')