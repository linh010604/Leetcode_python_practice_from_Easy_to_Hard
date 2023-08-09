class Solution(object):
    def canSplitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: bool
        """
        if len(nums) <= 2 :
            return True

        for i in range(1,len(nums)):
            csum = nums[i-1] + nums[i]
            if csum >= m :
                return True
            
        return False
        
