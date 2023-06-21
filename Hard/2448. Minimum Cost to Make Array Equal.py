def findcost(nums , cost , num) :
    n = len(nums)
    total = 0
    for i in range (n) :
        total += abs(nums[i] - num) * cost[i]

    return total

class Solution(object):
    def minCost(self, nums, cost):
        """
        :type nums: List[int]
        :type cost: List[int]
        :rtype: int
        """
        right = max(nums)
        left = min(nums)
        ans = 10E20 + 7

        while left <= right :
            mid = (left + right) / 2
            min1 = findcost(nums , cost , mid)
            min2 = findcost(nums , cost , mid + 1)
            ans = min(min1 , min2,ans)
            if min1 < min2 :
                right = mid - 1
            else :
                left = mid + 1

        return ans
