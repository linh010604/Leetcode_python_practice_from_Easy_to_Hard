class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n_str = ""
        count_l = dict()
        res = 0

        for i , letter in enumerate(s) :
            if letter not in n_str :
                count_l[letter] = i
                n_str += letter 
                res = max(res,len(n_str))
            else:
                res = max(res,len(n_str))
                n_str = s[count_l[letter]+1:i+1]
                count_l[letter] = i
                #n_str += letter
            print(n_str,res,count_l[letter],letter)

        return res
        
