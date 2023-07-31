class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        idx = 0 

        while idx < len(haystack) - len(needle) + 1:
                if haystack[idx:idx + len(needle)] == needle :
                    return idx
                
                idx += 1

        return -1
 
