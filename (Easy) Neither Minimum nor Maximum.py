class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nmin = min(nums)
        nmax = max(nums)
        
        for item in nums :
            if item != nmin and item != nmax :
                return item
        
        return -1
        
