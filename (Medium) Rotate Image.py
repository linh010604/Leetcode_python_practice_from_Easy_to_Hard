import copy
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        new = copy.deepcopy(matrix)

        n= len(matrix)

        for i in range (n) :

            for j in range (n - 1 , -1 , -1) :
            
                matrix[i][n -1 - j] = new[j][i] 

        return matrix
