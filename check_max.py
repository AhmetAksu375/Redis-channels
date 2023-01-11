import redis
import time

r = redis.Redis(host="localhost", port=6379, db=0)
p = r.pubsub()
p.subscribe("high_sum")
r.set("max_sum", 0)





def checkMaxFunc():
    ts = int(time.time() % 2)
    message = p.get_message()
    if(message != None): 
        max = int(message['data'])
        currentMax = int(r.get("max_sum"))
        if(ts == 0 and max > currentMax):
            r.set("max_sum", max)
            print("max set: " + str(max))


            
            

