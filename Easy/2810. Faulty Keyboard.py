class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        res = ""
        rev = ""
        crt = ""
        
        for idx, item in enumerate(s) :
            if item != "i" :
                res += item
            else :
                res = res[-1::-1]
                
        
        return res
        
