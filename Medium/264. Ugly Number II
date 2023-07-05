class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = [1]
        idx2 = 0
        idx3 = 0
        idx5 = 0 
        while len(d) < n:
            d.append(min(d[idx2]*2 , d[idx3]*3 , d[idx5]*5,))

            if d[-1] == d[-2] :
                d.pop()

            if d[-1] == d[idx2]*2 :
                idx2 += 1
            elif d[-1] == d[idx3]*3 :
                idx3 += 1
            elif d[-1] == d[idx5]*5 :
                idx5 += 1

        return d[-1]
        
