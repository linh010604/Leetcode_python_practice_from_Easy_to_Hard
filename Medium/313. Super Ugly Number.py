class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        primecnt = list(0 for i in range (len(primes)))

        d = [1]

        while len(d) < n :
            d.append(min(d[primecnt[i]]*primes[i] for i in range (len(primes) ) ) )
            #print(d)
            if d[-1] == d[-2] :
                d.pop()
            for i in range (len(primes)) :
                if d[-1] == d[primecnt[i]]*primes[i] :
                    primecnt[i] += 1
                    break

        return d[-1]
