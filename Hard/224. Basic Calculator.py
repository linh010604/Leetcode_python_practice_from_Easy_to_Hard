def combo (s , idx , signn) :
    res = 0
    i = 0
    sign = '+'
    i = idx + 1 
    while i < len(s) :
        if s[i] in '+-' :
            sign = s[i]
        elif s[i] == '(' :
            num,i = combo(s,i,sign)
            res += int(num)
        elif s[i] == ')' :
            if signn =='-' :
                return -res , i
            return res , i
        else :
            num = ""
            while s[i] in "0123456789" :
                num += s[i]
                i += 1
            i -= 1
            num = int(num)
            if sign == '+' :
                res += num
            else :
                res -= num
        i += 1
        
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ","")
        if s[0] != '-':
            s = '+' + s

        i = res = 0
        while i < len(s) :
            if s[i] in '+-' :
                sign = s[i]
            elif s[i] == '(' :
                num,i = combo(s,i,sign)
                res += int(num)
            elif s[i] == ')' :
                if signn =='-' :
                    return -res , i
                return res , i
            else :
                num = ""
                while i < len(s) and s[i] in "0123456789" :
                    num += s[i]
                    i += 1
                i -= 1
                if sign == '+' :
                    res += int(num)
                else :
                    res -= int(num)
            i += 1
    
        return res
