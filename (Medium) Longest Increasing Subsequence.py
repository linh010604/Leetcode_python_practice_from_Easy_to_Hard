'''
# This solution had complexity of O(n^2) since using 2 for loop
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = dict()
        res = 1

        d = list(1 for i in range(len(nums) + 1))

        for i in range (len(nums)) :
            for j in range(i) :
                if nums[j] < nums[i] :
                    d[i] = max(d[i] , d[j] + 1)
                res = max(res, d[i])

        return res
'''
# This solution had complexity of O(n log n). 
# dp[i] is the number end the strictly increasing sequence with length i and dp is an increasing array, 
# therefore, we can use BS to find this longest list satisfied.
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = dict()
        dp[1] = nums[0]

        for i in range (len(nums)) :
            left = 1
            right = len(dp) 
            tmp = 0

            while (left <= right) :
                mid = int((left + right) / 2)
                if dp[mid] <  nums[i] :
                    left = mid + 1
                    tmp = mid 
                else :
                    right = mid - 1
                    tmp = mid - 1

            dp[tmp+1] = min( nums[i] , dp.get(tmp+1,10010) )

        return len(dp)
