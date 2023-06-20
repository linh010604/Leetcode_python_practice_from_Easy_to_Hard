class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        res = list(-1 for i in range( min (k , len(nums) ) ) )
        total = sum(nums[:2*k])

        for idx in range(2*k , len(nums)) :
            total += nums[idx]
            res.append(total/(2*k+1))
            total -= nums[idx - 2*k]

        for i in range( min(k , len(nums) - k ) ) :
            res.append( -1 )

        return res
