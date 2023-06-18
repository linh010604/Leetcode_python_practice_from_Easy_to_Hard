class Solution(object):
    def findValueOfPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        
        res = 10E9 + 7
        
        for i in range (1 , len(nums)) :
            res = min(nums[i] - nums[i-1] , res)
            
        return res
        
