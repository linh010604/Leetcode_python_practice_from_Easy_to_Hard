class Solution(object):
    def numberOfGoodSubarraySplits(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        i = 0
        while i < len(nums) and nums[i] == 0 :
            i += 1
            
        if i == len(nums) :
            return 0
        
        res = 1
        cnt = 1
        while i < len(nums) :
            if nums[i] == 1 :
                res *= cnt
                res = res % (10**9 + 7)
                cnt = 1
            else :
                cnt += 1
            i += 1
                
        return int(res)
            
        
