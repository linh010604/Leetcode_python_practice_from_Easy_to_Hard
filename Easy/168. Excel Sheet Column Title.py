class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        res = ""
        d = '0ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        while columnNumber > 0 :
            n = columnNumber % 26
            if n == 0 :
                n = 26
                columnNumber -= 1
            res = d[n] + res
            columnNumber /= 26

        return res
