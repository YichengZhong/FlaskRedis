def string_get_func(key,redisConnect):
    result = redisConnect.get(key)
    return result

def string_set_func(key,value,redisConnect):
    result =redisConnect.set(key,value)
    return result

def string_mget_func(L_key,redisConnect):
    result =redisConnect.mget(L_key)
    return result

def string_mset_func(L_key,L_value,redisConnect):
    #保护
    if(len(L_key) != len(L_value)):
        return 0

    dict_key_value=dict(zip(L_key,L_value))
    result = redisConnect.mset(dict_key_value)

    return result

dic_string_commandswitch = {"string_getcommand":string_get_func,
                            "string_setcommand":string_set_func,
                            "key_mgetscommand":string_mget_func,
                            "string_msetcommand": string_mset_func}

def string_func(command,redisConnect):
    '''
    运行string命令
    :return:
    '''
    print('string_func')