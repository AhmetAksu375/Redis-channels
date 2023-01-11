import redis
import time

r = redis.Redis(host="localhost", port=6379, db=0)

p = r.pubsub()
p.subscribe("sum")
p.subscribe("high_sum")
p.subscribe("low_sum")



def setPublishSum(sum):
    r.publish("sum", sum)
    

def setPublishHighSum(sum):
    r.publish("high_sum", sum)

def setPublishLowSum(sum):
    r.publish("low_sum", sum)

def setMinSum(sum):
    r.set("min_sum", sum)

def setMaxSum(sum):
    r.set("max_sum", sum)

def flushAllFunc():
    time.sleep(3)
    r.flushall()