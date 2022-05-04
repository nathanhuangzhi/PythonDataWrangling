def singleNumber(nums):
    res = 0
    for n in nums:
        res = n ^ res
        print(res)
    return res


print(singleNumber([1,2,1]))