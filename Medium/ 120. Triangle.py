class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        height = len(triangle)
        INT_MAX = 10**9 + 7
        dp = list()


        for i in range (height) :
            dp.append(list())
            for j in range (len(triangle[i])) :
                dp[i].append(INT_MAX)

        dp[0][0] = triangle[0][0]

        for i in range (height-1) :
            for j in range(len(triangle[i])) :
                dp[i+1][j] = min(dp[i+1][j] , dp[i][j] + triangle[i+1][j] )
                dp[i+1][j+1] = min(dp[i+1][j+1] , dp[i][j] + triangle[i+1][j+1])

        return (min(dp[height-1])) 
