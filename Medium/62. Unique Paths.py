class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        d = deque() 
        d.append([0,0])

        dp = list()
        for i in range (m) :
            dp.append(list())
            for j in range (n) :
                dp[i].append(0)

        dp[0][0] = 1

        while len(d) != 0:
            tmp = d.popleft()
        
            if tmp[0] + 1 < m :
                if (dp[tmp[0]+1][tmp[1]] == 0) :
                    d.append([tmp[0] + 1 , tmp[1] ])
                dp[tmp[0]+1][tmp[1]] += dp[tmp[0]][tmp[1]]
            if tmp[1] + 1 < n :
                if (dp[tmp[0]][tmp[1]+1] == 0) :
                    d.append([tmp[0] , tmp[1]  + 1])
                dp[tmp[0]][tmp[1]+1] += dp[tmp[0]][tmp[1]]
      
        return dp[m-1][n-1]
