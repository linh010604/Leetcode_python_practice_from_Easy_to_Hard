def compute_pali(str,s,left,right,res) :

        while(left >= 0 and right < len(str) and str[left] == str[right] ):
            res += 2
            s = str[left] + s + str[right]
            left -= 1
            right += 1

        return res , s
class Solution(object):
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res_len = 0
        res_str = ""
        for i in range(len(s)):
            current_len , current_str = compute_pali(s,s[i],i-1,i+1,1)
            if current_len > res_len :
                res_len = current_len
                res_str = current_str

            current_len, current_str = compute_pali(s, "", i , i + 1, 0)
            if current_len > res_len:
                res_len = current_len
                res_str = current_str

        return (res_str)
