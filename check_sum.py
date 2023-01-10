import check_redis as redisPy


# function to check the sum and publish as high_sum and low_sum
def checkSum(sum):
    if( sum > 30000):
        redisPy.publishHighSum(sum)
    else:
        redisPy.publishLowSum(sum)