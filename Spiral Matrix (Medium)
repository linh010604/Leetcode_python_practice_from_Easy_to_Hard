class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = list ()

        right = len(matrix[0]) - 1
        down = len(matrix) -  1

        left = 0
        up = 0

        i = 0
        j = 0

        while left <= right and up <= down :
            for item in matrix[up][left:right + 1] :
                res.append(item)

            up += 1

            print(res)

            for idx in range (up,down+1) :
                res.append(matrix[idx][right])

            right -= 1

            print(res)

            if down != up  - 1 :
                for idx in range (right,left -1 ,-1):
                    res.append(matrix[down][idx])

            down -= 1

            print(res)

            if left != right + 1 :
                for idx in range (down , up - 1 , -1) :
                    res.append(matrix[idx][left])

            left += 1

            print(res)

        return res

