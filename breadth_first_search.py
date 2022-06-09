def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    sum_list = []
    large_list = []
    largest_sum = -9999999
    sum_num = -9999999
    for i in nums:

        if sum_num < 0:
            sum_num = i
            sum_list = [i]
            if largest_sum >= sum_num:
                continue

            else:
                large_list = sum_list
                largest_sum = sum_num

        else:
            sum_num += i
            sum_list.append(i)

            if largest_sum < sum_num:
                largest_sum = sum_num
                large_list = sum_list
            print(largest_sum,large_list)

    return largest_sum, large_list


print(maxSubArray([1,3,2,1,5,-1,9,-2,-5,1,-5,2,3]))

print(sum([1, 3, 2, 1, 5, -1, 9, -2, -5, 1, -5, 2, 3]))