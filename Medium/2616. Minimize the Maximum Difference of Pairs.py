class Solution(object):
    def minimizeMax(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        nums.sort()
        l = 0
        r = nums[-1] - nums[0]
        res = 0

        while l <= r :
            mid = (l + r)//2
            count = 0
            i = 1
            while i < len(nums) and count < p:
                if nums[i] - nums[i-1] <= mid :
                    count += 1
                    i += 1
                i += 1

            if count >= p :
                r = mid - 1
                res = mid
            else :
                l = mid + 1
                res = mid + 1

        return res
