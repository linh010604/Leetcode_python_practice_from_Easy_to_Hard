def DFS( idx , dp ) :
    d = deque()
    d.append(idx)
    check = list(0 for i in range (len(dp)))
    check[idx] = 1
    res = 0

    while len(d) != 0 :
        res += 1
        tmp = d.popleft()
        for i in range (len(dp[tmp])) :
            if check[ dp[tmp][i]  ] == 0:
                check[ dp[tmp][i]  ] = 1
                d.append( dp[tmp][i]  )

    return res

class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        res = 0
        dp = list()

        for i in range (len(bombs)) :
            dp.append(list())
            for j in range (len(bombs)) :
                if sqrt( (bombs[i][0] - bombs[j][0])**2 +  (bombs[i][1] - bombs[j][1])**2) <= bombs[i][2] :
                    dp[i].append(j)
        
        for i in range (len(bombs)) :
            res = max(DFS(i , dp),res)

        return res
