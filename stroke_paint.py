
class Solution(object):
    def maxOneArray(self ,nums ,n):
        n = 3
        length = len(nums)
        findmax = -99999
        for i in range(0 ,(length - n +1)):
            current_max = sum(nums[i:( i +n)])
            if current_max >findmax:
                findmax = current_max
        return(findmax)


    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arrymax = -99999999
        n = (round(len(nums ) /2))
        lowerbound = 0
        upperbound = len(nums)


        output = self.maxOneArray(nums ,n)
        while lowerbound != upperbound:
            if arrymax <= output:
                n = round((lowerbound +n ) /2)
                output = self.maxOneArray(nums ,n)
                lowerbound = n
            else:
                n = round((len(nums ) +upperbound ) /2)
                output = self.maxOneArray(nums ,n)
                upperbound = n
        return output

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))