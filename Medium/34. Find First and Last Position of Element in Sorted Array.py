class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0 :
            return [-1,-1]

        l = 0
        res = 0
        r = len(nums) - 1
        while l <= r :
            mid = int((l+r)/2)
            if nums[mid] < target :
                l = mid + 1 
                res = mid + 1 
            else :
                r= mid - 1
                res = mid

        if res >= len(nums) or nums[res] != target :
            return [-1,-1]

        ans = res

        l = 0
        res = 0
        r = len(nums) - 1
        while l <= r :
            mid = int((l+r)/2)
            if nums[mid] <= target :
                l = mid + 1 
                res = mid
            else :
                r= mid - 1
                res = mid - 1

        return [ans,res]
