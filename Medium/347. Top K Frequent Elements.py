class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = dict() 
        for item in nums :
            d[item] = d.get(item,0) + 1
        
        dp = sorted(d.items() , key = lambda x:x[1])
        idx = 0
        res = list()
        while k > 0 :
            k -= 1 
            idx -= 1
            res.append(dp[idx][0])
        return res
