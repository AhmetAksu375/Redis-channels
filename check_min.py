import check_redis as redisPy
import redis
import time

r = redis.Redis(host="localhost", port=6379, db=0)
p = r.pubsub()
p.subscribe("low_sum")



def checkMinFunc():
    ts = int(time.time() % 2)
    
    message = p.get_message()
    if(message != None): 

        min = int(message['data'])
        if(r.get("min_sum") == None):
            r.set("min_sum", min)

        currentMin = int(r.get("min_sum"))    
        if(currentMin == 1):
            r.set("min_sum", min)
        

        
        if(ts != 0 and min < currentMin):
            r.set("min_sum", min)
            print("min set: " + str(min))
                
