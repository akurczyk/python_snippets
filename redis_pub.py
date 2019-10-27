import time
import redis

r = redis.Redis()

while True:
    r.publish('aaa', 'bbb')
    time.sleep(5)
