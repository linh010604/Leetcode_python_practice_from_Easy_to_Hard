class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        d = list(list(0 for i in range (len(text2)+1)) for j in range(len(text1)+1))

        for i in range (len(text1)) :
            for j in range (len(text2)) :
                if text1[i] == text2[j] :
                    d[i+1][j+1] = d[i][j] + 1
                else :
                    d[i+1][j+1] = max(d[i][j+1],d[i+1][j])

        return d[-1][-1]
