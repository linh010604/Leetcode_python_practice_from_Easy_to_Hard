class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2 :
            return 0
        d = list(1 for i in range (n))
        d[1] = 0
        d[0] = 0
        for i in range ( 2 , int(sqrt(n)) + 1 ) :
            if d[i] == 1 :
                for j in range (i*i,n,i) :
                    d[j] = 0

        return sum(d)
