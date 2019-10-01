import redis
import time

r = redis.Redis()
ps = r.pubsub()
print(ps.subscribe('aaa'))

while True:
    print(ps.get_message())
    time.sleep(1)
