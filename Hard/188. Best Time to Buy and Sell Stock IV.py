class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int 
        """
        buy = list(list(-1000 for i in range (len(prices))) for j in range (k+1))
        sell = list(list(-1000 for i in range (len(prices))) for j in range (k))
        buy[0][0] = -prices[0]
        n = len(prices)
        res = 0

        for i in range (1,n) :
            buy[0][i] = max(-prices[i] , buy[0][i-1])
            for j in range (k) :
                if i >= 2*(j+1) :
                    buy[j+1][i] = max(sell[j][i-1] - prices[i] , buy[j+1][i-1])
                if i >= 2*(j+1)-1 :
                    sell[j][i] = max(buy[j][i-1] + prices[i] , sell[j][i-1])
            
                res = max(res,sell[j][-1])

        return res
