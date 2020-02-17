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

def hash_del_func(name, L_key,redisConnect):
    result = redisConnect.hdel(name, L_key)
    return result

dic_string_commandswitch = {"hash_getcommand":hash_get_func,
                            "hash_setcommand":hash_set_func,
                            "hash_mgetscommand":hash_mget_func,
                            "hash_msetcommand": hash_mset_func,
                            "hash_hexists":hash_hexists_func,
                            "hash_delcommand":hash_del_func}

def hash_func(command,redisConnect):
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

    if (L_command_words[0] == "hset" and len(L_command_words) == 4):
        name=L_command_words[1]
        key=L_command_words[2]
        value=L_command_words[3]
        result=hash_set_func(name,key,value,redisConnect)
        return result
    elif (L_command_words[0] == "hget" and len(L_command_words) == 3):
        name = L_command_words[1]
        key = L_command_words[2]
        result = hash_get_func(name, key,redisConnect)
        return result
    elif (L_command_words[0] == "hmset" and len(L_command_words) % 2 == 0 and len(L_command_words)>=6):
        name = L_command_words[1]
        L_key=L_command_words[2:len(L_command_words):2]
        L_value=L_command_words[3:len(L_command_words):2]
        result = hash_mset_func(name, L_key,L_value, redisConnect)
        return result
    elif (L_command_words[0] == "hmget" and len(L_command_words) >= 3):
        name = L_command_words[1]
        L_key = L_command_words[1:]
        result = hash_mget_func(name, L_key,redisConnect)
        return result
    elif (L_command_words[0] == "hexists" and len(L_command_words) == 3):
        name = L_command_words[1]
        key = L_command_words[2]
        result = hash_hexists_func(name, key, redisConnect)
        return result
    elif (L_command_words[0] == "hdel" and len(L_command_words) >= 3):
        name = L_command_words[1]
        L_key = L_command_words[1:]
        result = hash_del_func(name, L_key, redisConnect)
        return result
