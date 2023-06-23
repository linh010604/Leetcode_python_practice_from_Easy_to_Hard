class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 :
            return 0
        elif len(nums) == 2 :
            return max(nums[1]-nums[0] , nums[0] - nums[1])
        else:
            nums.sort()
            res = 0
            for i in range (1,len(nums)) :
                res = max(nums[i] - nums[i-1],res)

            return res
