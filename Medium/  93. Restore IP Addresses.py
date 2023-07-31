class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        res = []

        for i in range (1,4) :
            for j in range (1,4) :
                for k in range (1,4) :
                    try :
                        a = int(s[:i])
                        b = int(s[i:i+j])
                        c = int(s[i+j:i+j+k])
                        d = int(s[i+j+k:])
                    except:
                        continue

                    print(a,b,c,d)
                            
                    if a <= 255 and b <= 255 and c <= 255 and d <= 255 and len(str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d)) == len(s) + 3 :
                        res.append(str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d))

        return res
