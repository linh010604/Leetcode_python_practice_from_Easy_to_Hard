class Solution(object):
    def longestArithSeqLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #d[i][j] : length of the subsequence end at nums[i] and steps of length = j
        n = len(nums)
        res = 0
        d = list(dict() for i in range (n))
        for i in range (1,n) :
            for j in range (i) :
                d[i][nums[i]- nums[j]] = d[j].get(nums[i]- nums[j],1) + 1
                res = max(res,d[i][nums[i]- nums[j]])

        return res
