def do (n) :
    sumn = 0
    while n > 0 :
        sumn += (n%10)**2
        n = n//10

    return sumn

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        start = end = n

        end = do(n)

        while start != end :
            start = do(start)
            end = do(end)
            end = do(end)

        if start == 1 or end == 1 :
            return True

        return False
