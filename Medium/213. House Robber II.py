class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n= len(nums)
        d = [0] * (n)
        dd = [0] * n
        d[0] = nums[0]
        
        if n > 1 :
            d[1] = nums[1]
            dd[1] = nums[1]
        else :
            return d[0]

        if n > 2 :
            dd[2] = nums[2]
            d[2] = d[0] + nums[2]
        else :
            return max(nums)
        
        if n > 3 :
            dd[3] = dd[1] + nums[3]
        else :
            return max(nums)

        for i in range (3,n-1) :
            d[i] = max(d[i-2],d[i-3]) + nums[i]

        for i in range (4,n) :
            dd[i] = max(dd[i-2],dd[i-3]) + nums[i]

        return max(d[-2],d[-3] , dd[-1],dd[-2])
        
