class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        if len(s3) != len(s1) + len(s2) :
            return False

        d = [[False for i in range(len(s2)+1)] for j in range (len(s1)+1)]

        for i in range (len(s1)+1) :
            for j in range (len(s2)+1) :
                if j == 0 and i == 0 :
                    d[i][j] = True
                elif i == 0 :
                    d[i][j] = d[i][j-1] and s2[j-1] == s3[i + j - 1]
                elif j == 0 :
                    d[i][j] = d[i-1][j] and s1[i-1] == s3[i + j - 1]
                else:
                    d[i][j] = (d[i-1][j] and s1[i-1] == s3[i + j - 1]) or (d[i][j-1] and s2[j-1] == s3[i + j - 1])

        return d[-1][-1]
