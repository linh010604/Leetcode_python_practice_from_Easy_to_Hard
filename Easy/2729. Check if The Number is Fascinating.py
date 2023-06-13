class Solution(object):
    def isFascinating(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n*3 > 999:
            return False
        s = ""
        s += str(n) + str(2*n) + str(3*n)
        d = dict()

        for num in s :
            d[num] = d.get(num,0) + 1
            if d[num] > 1 or num == '0':
                return False
        return True
        
