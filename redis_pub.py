import redis
import time

r = redis.Redis()

while True:
    r.publish('aaa', 'bbb')
    time.sleep(5)
