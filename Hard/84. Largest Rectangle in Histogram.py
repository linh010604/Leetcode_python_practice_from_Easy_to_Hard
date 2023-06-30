class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        n = len(heights)

        right = list(0 for i in range(n))
        left = list(0 for i in range(n))
        left[0] = -1
        right[-1] = n

        for i in range (1, n) :
            p = i - 1
            while p >= 0 and heights[p] >= heights[i] :
                p = left[p]
            left[i] = p

        for i in range (n-2,-1,-1) :
            p = i + 1
            while p < n and heights[p] >= heights[i] :
                p = right[p]
            right[i] = p

        res = 0

        for i in range (n) :
            res = max(res , (right[i] - left[i]-1) * heights[i])

        return res
