class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        d = deque() 
        d.append([0,0])
        m = len(grid)
        n = len(grid[0])
        INT_MAX = 10E9 + 7

        dp = list()
        for i in range (m) :
            dp.append(list())
            for j in range (n) :
                dp[i].append(INT_MAX)

        dp[0][0] = grid[0][0]
        #print(dp)

        while len(d) != 0:
            tmp = d.popleft()
            #print(tmp)
            if tmp[0] + 1 < m :
                if (dp[tmp[0]+1][tmp[1]] == 10E9 + 7) :
                    d.append([tmp[0] + 1 , tmp[1] ])
                dp[tmp[0]+1][tmp[1]] = min(dp[tmp[0]][tmp[1]] + grid[tmp[0]+1][tmp[1]] , dp[tmp[0]+1][tmp[1]])
            if tmp[1] + 1 < n :
                if (dp[tmp[0]][tmp[1]+1] == 10E9 + 7) :
                    d.append([tmp[0] , tmp[1]  + 1])
                dp[tmp[0]][tmp[1]+1] = min(dp[tmp[0]][tmp[1]] + grid[tmp[0]][tmp[1]+1] , dp[tmp[0]][tmp[1]+1] )
        #print(dp)
        return dp[m-1][n-1]
