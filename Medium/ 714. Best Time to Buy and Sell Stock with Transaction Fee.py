class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """

        sell = 0
        buy = -prices[0]
        for i in range(1,len(prices)) :
            buy = max(sell - prices[i] , buy)
            sell = max(sell , buy + prices[i] - fee)

        return sell
