class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)

        idx = 0
        res = 0
        rotategrid = list()

        for i in range(n) :
            rotategrid.append(list())
            for j in range (n) :
                rotategrid[i].append(grid[j][i])

        for i in range(n) :
            for j in range (n) :
                if grid[i] ==  rotategrid[j] :
                    res += 1
 
        return res
            
