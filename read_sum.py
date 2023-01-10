import check_redis as redisPy
import check_sum as sumPy
import check_min as minPy
import check_max as maxPy
# Description: Reads a file and sums the numbers in the file
def checkSum():
    result = 0
    liste = []

    with open('input.txt') as f:
        for line in f:
            liste.append(line.strip())
        for a in liste:
            if(a == ""):
                #print(result)
                redisPy.publishSum(result)
                sumPy.checkSum(result)
                x = redisPy.p.get_message()
                maxPy.checkMax()
                minPy.checkMin()
                result = 0
            else:
                result += int(a)


checkSum()
redisPy.flushAll()