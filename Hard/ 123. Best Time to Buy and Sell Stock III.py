class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        buy = list(list(-100000 for i in range (len(prices))) for j in range (3))
        sell = list(list(-100000 for i in range (len(prices))) for j in range (2))
        buy[0][0] = -prices[0]
        n = len(prices)

        for i in range (1,n) :
            buy[0][i] = max(-prices[i] , buy[0][i-1])
            if i >= 2 :
                buy[1][i] = max(sell[0][i-1] - prices[i] , buy[1][i-1])
            if i >= 1 :
                sell[0][i] = max(buy[0][i-1] + prices[i] , sell[0][i-1])
            if i >= 4 :
                buy[2][i] = max(sell[1][i-1] - prices[i] , buy[2][i-1])
            if i >= 3 :
                sell[1][i] = max(buy[1][i-1] + prices[i] , sell[1][i-1])


        return max(sell[1][-1] , sell[0][-1] , 0)
