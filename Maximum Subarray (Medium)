class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = -10**9
        sum_ = 0 

        for i in range (len(nums)) :
            sum_ = max(sum_ + nums[i] , nums[i])
            res = max(res , sum_)

        return res
