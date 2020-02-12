def key_del_func(key,redisConnect):
    result =redisConnect.delete(key)
    return result

def key_scan_func(begincur,keypattern,limitsize,redisConnect):
    if(limitsize>=100):
        limitsize=100;

    result = redisConnect.scan(begincur,keypattern,limitsize)
    return_pos, datalist = result

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
    L_command_words = command.split(' ')
    if (len(L_command_words) < 2):
        print("command len is error\n")
        return

    if ( L_command_words[0] == "del"):
        pass
    elif ( L_command_words[0] == "exists" ):
        pass
    elif ( L_command_words[0] == "scan" ):
        pass