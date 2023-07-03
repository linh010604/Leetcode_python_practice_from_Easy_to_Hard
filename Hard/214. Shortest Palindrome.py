class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)%2==0 :
            idx = len(s)/2 - 1
        else :
            idx = len(s)/2

        while (s[:idx+1] != s[idx*2+1:idx:-1]) and  s[:idx+1] != s[idx*2+2:idx+1:-1]:
            idx -= 1
    
        if s[:idx+1] == s[idx*2+2:idx+1:-1] :
            return s[:idx*2+2:-1] + s
        elif s[:idx+1] == s[idx*2+1:idx:-1] :
            return s[:idx*2+1:-1] + s
        return s
        
