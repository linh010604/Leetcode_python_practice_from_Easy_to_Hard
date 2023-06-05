# Using dynamic programming
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        d = list()

        for idx in range(len(s)+1) :
            d.append(list())
            for idex in range(len(t)+1) :
                if idex == 0 :
                    d[idx].append(1)
                else :
                    d[idx].append(0)

        for idx in range(len(s)) :
            for idex in range(len(t)) :
                if s[idx] == t[idex] :
                    d[idx+1][idex+1] = d[idx][idex] + d[idx][idex+1]

                else :
                    d[idx+1][idex+1] = d[idx][idex+1] 

        return d[-1][-1]

    
    
