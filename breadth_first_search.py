def containdup(nums):

    num_range = set()
    for i in range(len(nums)):
        if nums[i] not in num_range:
            num_range.add(nums[i])
            print(num_range)
        else:
            return True

    return False

print(containdup([1,2,3,1]))