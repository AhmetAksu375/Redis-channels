import redis
import time

# Connect to Redis
r = redis.Redis(host="localhost", port=6379, db=0)

# Pub sub
p = r.pubsub()
p.subscribe("sum")
p.subscribe("high_sum")
p.subscribe("low_sum")



# function: publis sum to redis
def publishSum(sum):
    r.publish("sum", sum)
    

# function: publish high sum to redis
def publishHighSum(sum):
    r.publish("high_sum", sum)

# function: publish low sum to redis
def publishLowSum(sum):
    r.publish("low_sum", sum)

# function: set min_sum to redis
def setMinSum(sum):
    r.set("min_sum", sum)

# function: set max_sum to redis
def setMaxSum(sum):
    r.set("max_sum", sum)

# function: flush all keys in redis
def flushAll():
    time.sleep(3)
    r.flushall()