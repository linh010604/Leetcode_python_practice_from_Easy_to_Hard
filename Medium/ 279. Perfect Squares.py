class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = [100 for i in range(n+1)]
        d[0] = 0

        for item in range(1,n+1) :
            m = int(sqrt(item))+1
            for i in range(1,m):
                d[item] = min(d[item-i*i]+1,d[item])

        return d[n]
