class Solution(object):
    def maximumJumps(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        d = list( -1 for i in range (len(nums)))
        
        d[0] = 0
        d[-1] = -1
        
        for i in range (len(nums)) :
            for j in range (i) :
                if abs(nums[i] - nums[j]) <= target and d[j] != -1:
                    d[i] = max(d[i],d[j]+1)
                    
        return d[-1]
        
