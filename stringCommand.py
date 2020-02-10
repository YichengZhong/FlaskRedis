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
                            "string_mgetscommand":string_mget_func,
                            "string_msetcommand": string_mset_func}

def string_func(command,redisConnect):
    '''
    运行string命令
    :return:
    '''
    print('string_func')

    string_command_type = "string_wrong_command"
    L_command_words = command.split(' ')
    if (len(L_command_words) < 2):
        print("command len is error\n")
        return

    if(L_command_words[0]=="set" and len(L_command_words)==3):
        pass
    elif (L_command_words[0]=="get" and len(L_command_words)==2):
        pass
    elif (L_command_words[0]=="mset" and len(L_command_words)%2==1):
        pass
    elif (L_command_words[0]=="mget"):
        pass

