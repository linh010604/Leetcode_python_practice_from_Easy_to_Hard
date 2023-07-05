class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        m = len(matrix)
        n = len(matrix[0])
        res = 0

        d = list(list(0 for i in range(n)) for j in range(m))

        d[0] = list(int(matrix[0][i]) for i in range(n))

        for i in  range (1,m) :
            for j in range (0,n) :
                if matrix[i][j] == "1" :
                    d[i][j] = d[i-1][j] + 1

        for j in range(m) :
            right = list(0 for i in range(n))
            left = list(0 for i in range(n))
            left[0] = -1
            right[-1] = n

            for i in range (1, n) :
                p = i - 1
                while p >= 0 and d[j][p] >= d[j][i] :
                    p = left[p]
                left[i] = p

            for i in range (n-2,-1,-1) :
                p = i + 1
                while p < n and d[j][p] >= d[j][i] :
                    p = right[p]
                right[i] = p

            rowres = 0

            for i in range (n) :
                rowres = max(rowres , (right[i] - left[i]-1) * d[j][i])

            res = max(res,rowres)

        return res
