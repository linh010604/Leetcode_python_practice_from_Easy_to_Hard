class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rowpos = set()
        colpos = set()
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m) :
            for j in range(n) :
                if matrix[i][j] == 0 :
                    rowpos.add(i)
                    colpos.add(j)

        for item in rowpos :
            for i in range (n) :
                matrix[item][i] = 0

        for item in colpos :
            for i in range (m) :
                matrix[i][item] = 0
