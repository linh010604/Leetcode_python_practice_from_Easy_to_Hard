class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = deque()
        res = list()
        for i in range(len(nums)) :
            if d and d[0] == i - k :
                d.popleft()
            while d and nums[d[-1]] < nums[i] :
                d.pop()
            d.append(i)
            if i >= k - 1 :
                res.append(nums[d[0]])
        return res
