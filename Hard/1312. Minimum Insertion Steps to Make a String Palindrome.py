class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        s1 = s[-1::-1]
        n = len(s)
        d = list(list(0 for i in range (n + 1)) for j in range (n + 1))

        for i in range (n) :
            for j in range (n) :
                if s[i] == s1[j] :
                    d[i+1][j+1] = d[i][j] + 1
                else :
                    d[i+1][j+1] = max(d[i+1][j] , d[i][j+1])


        return n - d[-1][-1]
