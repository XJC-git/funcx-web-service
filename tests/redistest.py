import redis
if __name__=="__main__":
    redis_client = redis.StrictRedis(
        host="r-wz9bivzhgo5pu53cb2.redis.rds.aliyuncs.com",
        port=6379,
        password="r-wz9bivzhgo5pu53cb2:70Xc1227",
        decode_responses=True,
    )
    redis_client.set('foo', 'bar')