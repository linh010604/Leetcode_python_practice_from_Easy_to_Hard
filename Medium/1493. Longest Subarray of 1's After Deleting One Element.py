class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt1 = 0
        cnt2 = 0
        res = 0
        idx = 0 

        while idx < len(nums) :
            if nums[idx] == 0 :
                res = max(res , cnt1 + cnt2)
                cnt2 = cnt1
                cnt1 = 0
            else :
                cnt1 += 1

            idx += 1

        res = max(res, cnt1 + cnt2)
        if cnt1 == len(nums) :
            return cnt1 - 1

        return res
