class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        if len(nums) == 1 :
            return 0

        for idx in range (len(nums)) :
            if (idx == 0 and nums[idx] > nums[idx+1]) or (idx == len(nums) - 1 and nums[idx] > nums[idx - 1]) or (0 < idx < len(nums) and nums[idx-1] < nums[idx] > nums[idx+1]) :
                return idx
