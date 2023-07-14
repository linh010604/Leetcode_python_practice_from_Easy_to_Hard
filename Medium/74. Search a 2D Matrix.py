class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: intx
        :rtype: bool
        """
        i = 0
        for i in range (len(matrix)) :
            if matrix[i][0] > target :
                i -= 1
                break

        l = 0
        r = len(matrix[i]) - 1
        mid = 0

        while l <= r :
            mid = (l+r)/2
            if matrix[i][mid] < target :
                l = mid + 1
            elif matrix[i][mid] > target :
                r = mid - 1
            else :
                break

        if matrix[i][mid] == target :
            return True

        return False
