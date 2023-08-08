class Solution(object):
    def numMusicPlaylists(self, n, goal, k):
        """
        :type n: int
        :type goal: int
        :type k: int
        :rtype: int
        """

        mod = 10**9+7

        d = [[0 for i in range (n+1)] for j in range (goal+1)]
        d[0][0] = 1
        for i in range (1,goal+1) :
            for j in range(1,n+1) :
                d[i][j] = (d[i-1][j-1] * (n - (j - 1))) % mod
                if j > k :
                    d[i][j] = (d[i][j] + (d[i-1][j] * (j-k))% mod) % mod

        return int(d[-1][-1] % mod)
                    
