class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        res = len(nums)
        total = nums[0]
        ok = True
        
        end = 0
        start = 0

        while end < len(nums) and start < len(nums):
            if total < target and end + 1 < len(nums):
                end += 1
                total += nums[end]
            elif total >= target :
                res = min(res , end - start+1)
                total -= nums[start]
                start += 1
                ok = False
            else :
                break

        if ok :
            return 0
        return res
