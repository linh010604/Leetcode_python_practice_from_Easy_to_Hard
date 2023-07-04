def check (num) :
    if len(str(num)) > 9 :
       return " Billion"
    elif len(str(num)) > 6 :
        return " Million"
    elif len(str(num)) > 3 :
        return " Thousand"
    return ""
    
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """

        d = { 1 : "One" , 2 : "Two" , 3 : "Three" , 4 : "Four" , 5 : "Five" , 6 : "Six" , \
        7: "Seven" , 8 : "Eight" , 9 : "Nine" , 10 : "Ten" , 11 : "Eleven" , 12 : "Twelve"\
        , 13 : "Thirteen" , 14 : "Fourteen" , 15 : "Fifteen" , 16 : "Sixteen" , \
        17 : "Seventeen" , 18 : "Eighteen", 19 : "Nineteen", 20 : "Twenty", \
        30 : "Thirty" , 40 : "Forty", 50 : "Fifty", 60 : "Sixty", \
        70 : "Seventy", 80 : "Eighty" , 90 : "Ninety"}

        res = ""

        if (num == 0) :
            return "Zero"

        while (num > 0) :

                if len(str(num)) % 3 == 1 :
                    res += " " + d[num/10** ( len(str(num)) - 1 )] 
                    res += check(num)
                    
                    num = num % 10** ( len(str(num)) - 1 )
                elif len(str(num)) % 3 == 2 :
                    if num/10** ( len(str(num)) -1 ) == 1 :
                        res += " " + d[num/10** ( len(str(num)) - 2 )] 

                        res += check(num)

                        num = num % 10** ( len(str(num)) - 2 )
                    else :
                        res += " " + d[num/10** ( len(str(num)) - 1 ) * 10]
                        
                        if num/10** ( len(str(num)) - 2 ) % 10 == 0 :
                            res += check(num)
                        num = num % 10** ( len(str(num)) - 1 )
                else :
                    res += " " + d[num/10** ( len(str(num)) - 1) ] + " Hundred"
                    if num/10** ( len(str(num)) - 3 ) % 100 == 0 :
                        res += check(num)
        
                    num = num % (10** ( len(str(num)) - 1))

        return res[1:]
