def check ( i , j , x , y , grid , ok , d) :
    if 0 <= x < len(grid) and 0 <= y < len(grid) and grid[x][y] == 0:
        if ok[x][y] == 10E9 + 7 :
            d.append([x,y])
        ok[x][y] = min(ok[x][y] , ok[i][j] + 1)

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1 
        else :
            d = deque()
            d.append([0,0])
            ok = list()
            n = len(grid)
            for i in range ( n ) :
                ok.append(list())
                for j in range ( n ) :
                    ok[i].append(10E9+7)

            ok[0][0] = 1 

            while(len(d) != 0) :
                tmp = d.popleft()
                check(tmp[0] , tmp[1] , tmp[0] - 1 , tmp[1] , grid , ok , d)
                check(tmp[0] , tmp[1] , tmp[0] - 1 , tmp[1] - 1, grid , ok , d)
                check(tmp[0] , tmp[1] , tmp[0] - 1 , tmp[1] + 1, grid , ok , d)
                check(tmp[0] , tmp[1] , tmp[0] , tmp[1] - 1, grid , ok , d)
                check(tmp[0] , tmp[1] , tmp[0] , tmp[1] + 1, grid , ok , d)
                check(tmp[0] , tmp[1] , tmp[0] + 1 , tmp[1] + 1, grid , ok , d)
                check(tmp[0] , tmp[1] , tmp[0] + 1 , tmp[1] , grid , ok , d)
                check(tmp[0] , tmp[1] , tmp[0] + 1 , tmp[1] - 1, grid , ok , d)

        if ok[-1][-1] == 10E9 + 7 :
            return -1
        return ok[-1][-1]
            
