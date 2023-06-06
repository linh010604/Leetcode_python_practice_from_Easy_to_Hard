class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        s1 = s[-1::-1]

        m = len(s)
        d= list()

        for i in range (m+1) :
            d.append(list())
            for j in range(m+1) :
                d[i].append(0)

        for i in range (1,m+1) :
            for j in range(1,m+1) :
                if s[i-1] == s1[j-1] :
                    d[i][j] = d[i-1][j-1] + 1
                else :
                    d[i][j] = max(d[i][j-1],d[i-1][j])

        #print (d)
        return d[-1][-1]
