class Solution(object):
    def longestString(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        
        if x == y :
            return 2 * (x + y + z)
        elif x > y :
            return 2 * (y + 1 + y + z)
        else :
            return 2 *(x + x + 1 + z)
        
