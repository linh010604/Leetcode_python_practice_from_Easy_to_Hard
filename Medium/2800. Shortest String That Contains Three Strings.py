def merge (a,b) :
    i = 0
    if a in b :
        return b
    if b in a :
        return a
    for i in range (min(len(a),len(b)),0,-1) :
        if a[-i:] == b[:i]:
            return a + b[i:]

    return a + b

def check (a,b,c) :
    return merge(merge(a,b) , c), merge(a,merge(b,c))
class Solution(object):
    def minimumString(self, a, b, c):
        """
        :type a: str
        :type b: str
        :type c: str
        :rtype: str
        """

        d = list(check(a,b,c)+ check(a,c,b)+ check(b,c,a)+ check(b,a,c)+ check(c,a,b)+ check(c,b,a))
    
        d.sort()
        d.sort(key = len)

        return d[0]
