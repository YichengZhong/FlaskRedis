def hash_get_func(name, key, redisConnect):
    result =redisConnect.hget(name, key)
    return result

def hash_set_func(name, key, value,redisConnect):
    result =redisConnect.hset(name, key,value)
    return result

def hash_mget_func(name, L_key, redisConnect):
    result =redisConnect.hmget(name, L_key)
    return result

def hash_mset_func(name, L_key,L_value,redisConnect):
    if (len(L_key) != len(L_value)):
        return 0

    dict_key_value = dict(zip(L_key, L_value))
    result =redisConnect.hmset(name, dict_key_value)
    return result

def hash_hexists_func(name, key,redisConnect):
    result =redisConnect.hexists(name, key)
    return result

def hash_del_func(name, key,redisConnect):
    result = redisConnect.hdel(name, key)
    return result

dic_string_commandswitch = {"hash_getcommand":hash_get_func,
                            "hash_setcommand":hash_set_func,
                            "hash_mgetscommand":hash_mget_func,
                            "hash_msetcommand": hash_mset_func,
                            "hash_hexists":hash_hexists_func,
                            "hash_delcommand":hash_del_func}

def hash_func(command):
    '''
    运行hash命令
    :return:
    '''
    print('hash_func')

    hash_command_type = "hash_wrong_command"
    L_command_words = command.split(' ')
    if (len(L_command_words) < 2):
        print("command len is error\n")
        return

    if (L_command_words[0] == "set" and len(L_command_words) == 3):
        pass
    elif (L_command_words[0] == "get" and len(L_command_words) == 2):
        pass
    elif (L_command_words[0] == "mset" and len(L_command_words) % 2 == 1):
        pass
    elif (L_command_words[0] == "mget"):
        pass
