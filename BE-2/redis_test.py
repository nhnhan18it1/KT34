from redis import Redis

re = Redis(host="192.168.233.128",port=6379,password=123)
re.set("hello","abc1")