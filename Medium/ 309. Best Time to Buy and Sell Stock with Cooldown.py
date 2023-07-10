class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        n = len(prices)

        buy = list(0 for i in range (n))
        sell = list(0 for i in range (n))
        buy[0] = -prices[0]
        for i in range(1,n) :
            buy[i] = max(sell[i-2] - prices[i] , buy[i-1])
            sell[i] = max(sell[i-1] , buy[i-1] + prices[i])

        return sell[-1]
