class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        sell = 0 
        buy = -prices[0]
        n = len(prices)

        for i in range (1,n) :
            buy = max(sell - prices[i] , buy)
            sell = max(buy + prices[i] , sell)

        return sell
