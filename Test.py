import redis
r=redis.StrictRedis(host="192.168.160.140",port=6379,db=0)

def key_func(command):
    '''
    运行key命令
    :return:
    '''
    print('key_func')

def string_func(command):
    '''
    运行string命令
    :return:
    '''
    print('string_func')

def hash_func(command):
    '''
    运行hash命令
    :return:
    '''
    print('third_func')

dic_commandswitch = {"key_command":key_func,"string_command":string_func,"hash_command":hash_func}

def commandTran(command):
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
