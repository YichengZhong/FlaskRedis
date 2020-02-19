def key_del_func(key,redisConnect):
    result =redisConnect.delete(key)
    return result

def key_scan_func(begincur,keypattern,limitsize,redisConnect):
    if(limitsize>=100):
        limitsize=100

    result = redisConnect.scan(begincur,keypattern,limitsize)
    return_pos, datalist = result

def key_exists_func(key,redisConnect):
    result = redisConnect.exists(key)
    return result

dic_key_commandswitch = {"key_delcommand":key_del_func,
                         "key_scancommand":key_scan_func,
                         "key_existscommand":key_exists_func}

def key_func(command,redisConnect):
    '''
    运行key命令
    :return:
    '''
    print('key_func')
    L_command_words = command.split(' ')
    if (len(L_command_words) < 2):
        print("command len is error\n")
        return

    if ( L_command_words[0] == "del" and len(L_command_words) == 2):
        name = L_command_words[1]
        result = key_del_func(name,redisConnect)
        return result
    elif ( L_command_words[0] == "exists" and len(L_command_words) == 2 ):
        pass
    elif ( L_command_words[0] == "scan" ):
        pass