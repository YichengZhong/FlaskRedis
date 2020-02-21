from __init_redis__ import redisConnect
from keyCommand import key_func
from stringCommand import string_func
from hashCommand import hash_func
from wrongCommand import wrong_func

dic_commandswitch = {"key_command":key_func,
                     "string_command":string_func,
                     "hash_command":hash_func,
                     "wrong_command":wrong_func}

L_key_command_keywords=["del","scan","exists"]
L_string_command_keywords=["set","get","mset","mget"]
L_hash_command_keywords=["hset","hget","hmset","hmget","hexists","hdel"]

def commandTran(command,redisConnect):
    '''
    根据命令选择指令
    :param command:
    :return:
    '''
    L_command_words = command.split(' ')
    if(len(L_command_words)<2):
        print("command len is error\n")
        return

    command_type="wrong_command"

    if(L_command_words[0] in L_key_command_keywords):
        command_type="key_command"
    elif (L_command_words[0] in L_string_command_keywords):
        command_type= "string_command"
    elif (L_command_words[0] in L_hash_command_keywords):
        command_type="hash_command"
    else:
        command_type = "wrong_command"

    try:
        result=dic_commandswitch[command_type](command,redisConnect) #执行相应的方法
        print(result)
    except KeyError as e:
        print("command is error")

if __name__ == '__main__':
    commandTran("set runoobkey redis",redisConnect)
    commandTran("get runoobkey", redisConnect)
    commandTran("mset runoobkey1 redis1 runoobkey2 redis2", redisConnect)
    commandTran("mget runoobkey1 runoobkey2 runoobkey3", redisConnect)
    commandTran("del runoobkey1 ", redisConnect)
