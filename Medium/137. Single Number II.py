class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 :
            return nums[-1]
        nums.sort()

        for i in range (1,len(nums)-1) :
            if nums[i] != nums[i-1] and nums[i] != nums[i+1] :
                return nums[i]

        if nums[-1] == nums[-2] :
            return nums[0]
        return nums[-1]
