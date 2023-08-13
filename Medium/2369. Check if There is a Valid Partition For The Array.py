class Solution(object):
    def validPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = [0 for i in range (len(nums)+1)]
        d[0] = 1
        d[1] = 0
        if nums[1] == nums[0] :
            d[2] = 1
        
        for i in range (2,len(nums)):
            if nums[i] == nums[i-1] :
                d[i+1] = d[i-1]
            if nums[i] == nums[i-1] == nums[i-2] :
                d[i+1] = max(d[i+1],d[i-2])
            if nums[i] == nums[i-1] + 1 == nums[i-2] + 2 :
                d[i+1] = max(d[i+1],d[i-2])

        return d[-1]

         
