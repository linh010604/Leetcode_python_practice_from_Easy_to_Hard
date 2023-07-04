class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n= len(nums)
        d = [0] * (n+2)
        d[0] = nums[0]
        if n > 1 :
            d[1] = nums[1]
        else :
            return d[0]

        for i in range (2,n) :
            d[i] = d[i-2] + nums[i]
            for j in range (i-1) :
                d[i] = max(d[j] + nums[i] , d[i] )
        
        return max(d[n-1] , d[n-2])
        
