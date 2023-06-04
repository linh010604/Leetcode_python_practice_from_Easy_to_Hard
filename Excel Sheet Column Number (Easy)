class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        s = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        idx = 0
        n = 0
        while idx < len(columnTitle) :
            n += s.index(columnTitle[idx]) * 26**(len(columnTitle) - 1 - idx) 
            idx += 1
        return n
