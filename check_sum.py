import check_redis as redisPy


def checkSumFunc(sum):
    if(sum > 30000):
        redisPy.setPublishHighSum(sum)
    else:
        redisPy.setPublishLowSum(sum)