import check_redis as redisPy
import check_sum as sumPy
import check_min as minPy
import check_max as maxPy
def checkSum():
    result = 0
    liste = []

    with open('input.txt') as f:
        for line in f:
            liste.append(line.strip())
        for a in liste:
            if(a == ""):
                redisPy.setPublishHighSum(result)
                sumPy.checkSumFunc(result)
                x = redisPy.p.get_message()
                maxPy.checkMaxFunc()
                minPy.checkMinFunc()
                result = 0
            else:
                result += int(a)


checkSum()
redisPy.flushAllFunc()