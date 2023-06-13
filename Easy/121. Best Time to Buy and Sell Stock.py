class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """  

        maxx = prices[0]
        minn = prices[0]
        res = 0
        for i in range(len(prices)) :
            if prices[i] > maxx :
                maxx = prices[i] 
                res = max(res,0,maxx-minn)
            elif prices[i] < minn :
                minn = prices[i]
                maxx = prices[i]

        return res
