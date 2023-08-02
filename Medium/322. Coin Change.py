class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        d = [100000 for i in range(amount+1)]
        d[0] = 0

        for idx in range (1,amount + 1) :
            for item in coins :
                if idx - item >= 0 and d[idx - item] != 100000 :
                    d[idx] = min(d[idx-item] + 1,d[idx])

        if d[-1] == 100000:
            d[-1] = -1
        return d[-1]
