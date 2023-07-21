class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        d = list()
        res = 0

        for i in range (m) :
            d.append(list())
            for j in range (n) :
                d[i].append(0)

        for i in  range (m) :
            for j in range (n) :
                if matrix[i][j] == '1' : 
                    if i == 0 or j == 0 :
                        d[i][j] = 1
                    else :
                        d[i][j] = min(d[i-1][j-1],d[i-1][j],d[i][j-1]) + 1

                res = max(res,d[i][j])

        return res*res
            
