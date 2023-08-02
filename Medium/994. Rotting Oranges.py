class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        n = len(grid[0])
        d = deque()
        R = [-1,0,1,0]
        C = [0,1,0,-1]
        cnt = 0
        res = 0

        for i in range(m) :
            for j in range(n) :
                if grid[i][j] == 2 :
                    d.append( [i,j,0] )
                elif grid[i][j] == 1 :
                    cnt += 1

        while len(d) > 0 :
            q = d.popleft()
            for i in range(4) :
                if 0 <= q[0] + R[i] < m and 0 <= q[1] + C[i] < n and grid[ q[0] + R[i] ][ q[1] + C[i] ] == 1:
                    grid[ q[0] + R[i] ][ q[1] + C[i] ] = 2
                    d.append( [q[0] + R[i] , q[1] + C[i] , q[2] + 1] )
                    res = max(res, q[2] + 1)
                    cnt -= 1
        if cnt > 0 :
            return -1
        return res


