class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = list()
        res.append([1])

        for i in range (1,numRows) :
            res.append(list())
            res[i].append(1)

            for j in range (i-1) :
                res[i].append(res[i-1][j+1]+res[i-1][j])

            res[i].append(1)

        return res
