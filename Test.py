import redis
r=redis.StrictRedis(host="192.168.160.128",port=6380,db=0)

r.set('foo','1')
a=r.get('foo')
print(a)
r.incr('foo','1')
a=r.get('foo')
print(a)

dic={"IPINFO":"10.43.83.106","IPTYPE":"IPV4","UPF":"UPF1"}
r.hmset("1000",dic)

li=["IPINFO","IPTYPE"]
print(r.hmget("1000",li))
print(r.hgetall("1000"))
# print("测试代码\n")