class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if("inf" in s.lower()):
            return False
        try :
            s = float(s)
            return True
        except :
            return False
