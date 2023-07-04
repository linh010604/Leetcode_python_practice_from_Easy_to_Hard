class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
    
        envelopes.sort(key = lambda x: (x[0],-x[1]))

        d = dict()
        d[1] = envelopes[0]

        for i in range (1,len(envelopes)) :
            end = len(d)
            start = 1
            res = 0

            while start <= end :
                mid = (start + end) / 2
                if d[mid][0] < envelopes[i][0] and  d[mid][1] < envelopes[i][1]:
                    res = mid
                    start = mid + 1
                else :
                    res =  mid-1
                    end = mid - 1

            d[res+1] = envelopes[i]

        return len(d)
