import redis
import json

r = redis.Redis()

# STRINGS
print('STRINGS')
print(r.set('aaa', 'bbb'))
print(r.get('aaa'))
print(r.delete('aaa'))
print(r.get('aaa'))
print()

# LISTS
print('LISTS')
print(r.lpush('aaa', 123))
print(r.rpush('aaa', 321))
print(r.lrange('aaa', 0, 100))
print(r.lpop('aaa'))
print(r.rpop('aaa'))
print()

# SETS
print('SETS')
print(r.sadd('aaa', '111'))
print(r.sadd('aaa', '222'))
print(r.sadd('aaa', '222'))
print(r.smembers('aaa'))
print(r.sadd('bbb', '111'))
print(r.sadd('bbb', '333'))
print(r.smembers('bbb'))
print(r.sdiff('aaa', 'bbb'))
print(r.sinter('aaa', 'bbb'))
print(r.sunion('aaa', 'bbb'))
print()

# HASHES
print('HASHES')
pipe = r.pipeline()
pipe.hset('ccc', 'abc', 123)
pipe.hset('ccc', 'bcd', 234)
pipe.hset('ccc', 'cde', 345)
pipe.hset('ccc', 'def', 456)
pipe.hgetall('ccc')
pipe.hget('ccc', 'abc')
print(pipe.execute())
print()

# JSON
print('JSON')
ddd = [{'aaa': 111, 'bbb': 222}, 'aaa', 'bbb']
print(r.set('ddd', json.dumps(ddd)))
print(json.loads(r.get('ddd')))

# CLEANUP
r.flushall()
