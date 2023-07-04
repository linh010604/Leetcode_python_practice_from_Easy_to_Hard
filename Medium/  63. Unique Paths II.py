class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 :
            return 0

        d = deque() 
        dp = list()

        for i in range (m) :
            dp.append(list())
            for j in range (n) :
                dp[i].append(0)

        d.append([0,0])
        dp[0][0] = 1

        while len(d) != 0 :
            tmp = d.popleft()
            if tmp[0] + 1 < m and obstacleGrid[tmp[0] + 1][tmp[1]] == 0 :
                if dp[tmp[0] + 1][tmp[1]] == 0 :
                    d.append([ tmp[0] + 1 , tmp[1] ])
                dp[tmp[0]+1][tmp[1]] += dp[tmp[0]][tmp[1]]
            if tmp[1] + 1 < n and obstacleGrid[tmp[0]][tmp[1]+1] == 0:
                if (dp[tmp[0]][tmp[1]+1] == 0) :
                    d.append([tmp[0] , tmp[1]  + 1])
                dp[tmp[0]][tmp[1]+1] += dp[tmp[0]][tmp[1]]

        return dp[m-1][n-1]
