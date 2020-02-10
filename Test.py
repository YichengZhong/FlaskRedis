from __init_redis__ import redisConnect
from keyCommand import key_func
from stringCommand import string_func
from hashCommand import hash_func

dic_commandswitch = {"key_command":key_func,
                     "string_command":string_func,
                     "hash_command":hash_func}

L_key_command_keywords=["del","scan","exists"]
L_string_command_keywords=["set","get","mset","mget"]
L_hash_command_keywords=["hset","hget","hmset","hmget","hexists","hdel"]

def commandTran(command,redisConnect):
    '''
    根据命令选择指令
    :param command:
    :return:
    '''
    try:
        dic_commandswitch["key_command"](command) #执行相应的方法
    except KeyError as e:
        print("command is error")

if __name__ == '__main__':
    commandTran("12")
