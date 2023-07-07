class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = dict()
        c = dict()
        restr = ""
        cnt = 0
        n = len(s)
        for item in t :
            d[item] = 0
            c[item] = c.get(item,0) + 1

        start = 0
        res = n

        for idx in range(n) :
            try :
                d[s[idx]] += 1
                if d[s[idx]] <= c[s[idx]] :
                    cnt += 1

                while cnt == len(t) :
                    res = min(res,idx - start + 1)
                    if res == idx - start + 1 :
                        restr = s[start:idx+1]

                    d[s[start]] -= 1
                    if d[s[start]] < c[s[start]] :
                        cnt -= 1
                    elif cnt == 0 :
                        start = idx
                    start += 1
                    while d.get(s[start] , -1) == -1 :
                        start += 1       
            except :
                if cnt == 0 :
                    start += 1
        return restr
