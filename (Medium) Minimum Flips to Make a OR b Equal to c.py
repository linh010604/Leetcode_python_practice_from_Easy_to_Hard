def numtobase( N, B ): 
    '''
    Convert decimal number to other base sytem , N(int), B(int)
    Value: 
        N (int) - the number need to be converted
        B (int) - the base of the new number from N
    Return:
        s (str) - a string representing the number N in base B, 
        must have length multiple of 8
    '''
    s = ""
        
    if N == 0 : # if N equals 0 return empty string
        return s
    
    while N > 0: # while quoitent > 0
        remain = N % B # divide the decimal number to be converted by the value of the new base
        s = str(remain) + s # get the remainder as the rightmost digit
        N = N // B # divide the quotient of the previous divide by the new base
        
    return s # return string with 0

class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        atr = numtobase(a,2)
        btr = numtobase(b,2)
        ctr = numtobase(c,2)

        length = max(len(atr), len(btr) , len(ctr))

        atr = atr.zfill(length)
        btr = btr.zfill(length)
        ctr = ctr.zfill(length)

        res = 0

        for i in range (length) :
            if atr[i] == '1' and btr[i] == '1' and ctr[i] == '0' :
                res += 2
            elif atr[i] == '0' and btr[i] == '0' and ctr[i] == '1' :
                res += 1
            elif atr[i] == '0' and btr[i] == '1' and ctr[i] == '0' :
                res += 1
            elif atr[i] == '1' and btr[i] == '0' and ctr[i] == '0' :
                res += 1
            
        return res
