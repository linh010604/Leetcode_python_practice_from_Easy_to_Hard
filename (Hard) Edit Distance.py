class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        m = len(word1)
        n = len(word2)
        d= list()

        for i in range (m+1) :
            d.append(list())
            for j in range(n+1) :
                d[i].append(i)
                d[0][j] = j

        for i in range (1,m+1) :
            for j in range(1,n+1) :
                if word1[i-1] == word2[j-1] :
                    d[i][j] = d[i-1][j-1] 
                else :
                    d[i][j] =  min(d[i-1][j-1] , d[i-1][j] , d[i][j-1] ) + 1

        #print (m , n , d)
        return d[-1][-1] 
