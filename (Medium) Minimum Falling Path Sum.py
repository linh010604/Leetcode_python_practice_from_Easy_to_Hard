class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n= len(matrix[0])
        d = list()
        d.append(list())

        for j in range(n) :
            d[0].append(matrix[0][j])
        
        for i in range (1,m) :
            d.append(list())
            for j in range(n) :
                d[i].append(10010)

        for row in range (m-1) :
            for col in range(n) :
                if col-1 > -1 :
                    d[row + 1][col - 1] = min(d[row + 1][col - 1], d[row][col] + matrix[row + 1][col - 1])

                if col+1 < n :
                    d[row + 1][col + 1] = min(d[row + 1][col + 1], d[row][col] + matrix[row + 1][col + 1])
                
                d[row + 1][col] = min(d[row + 1][col], d[row][col] + matrix[row + 1][col])

        return min(d[-1])
