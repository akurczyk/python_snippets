import time
import redis

r = redis.Redis()
ps = r.pubsub()
print(ps.subscribe('aaa'))

while True:
    print(ps.get_message())
    time.sleep(1)
