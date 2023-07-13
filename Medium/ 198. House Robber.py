class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n= len(nums)
        d = [0] * (n)
        d[0] = nums[0]
        if n > 1 :
            d[1] = nums[1]
        else :
            return d[0]

        for i in range (2,n) :
            d[i] = max(d[i-2],d[i-3]) + nums[i]
        
        return max(d[-1] , d[-2])
        
