def binary_search(arr,ele):

    mid = len(arr)//2
    if ele == arr[mid]:
        return True

    elif ele < arr[mid]:
        return binary_search(arr[:mid],ele)

    else:
        return binary_search(arr[mid+1:],ele)

# print(binary_search([-1,0,3,5,9,12],9))


def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    mid = len(nums)//2
    if target == nums[mid]:
        return True



    elif target < nums[mid]:

        return(search(nums[:mid], target))

    else:
        return(search(nums[mid+1:], target))


print(search([-1,0,3,5,9,12],9))

