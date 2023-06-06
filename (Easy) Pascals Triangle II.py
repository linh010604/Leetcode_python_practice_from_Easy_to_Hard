class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        res = list()
        res.append([1])

        for i in range (1,rowIndex+1) :
            res.append(list())
            res[i].append(1)

            for j in range (i-1) :
                res[i].append(res[i-1][j+1]+res[i-1][j])

            res[i].append(1)

        return res[rowIndex]
