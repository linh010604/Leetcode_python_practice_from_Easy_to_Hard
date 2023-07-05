class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = 1
        for index in range (len(nums)-1):
            if nums[index] == nums[index+1] :
                nums[index] = 200
            else:
                r += 1
        
        nums.sort()
        
        return r

