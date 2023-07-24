class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        res = list()
        n = len(intervals)

        if n == 1 :
            return intervals

        start = intervals[0][0]
        end = intervals[0][1]
        idx = 1

        while idx < n :
            if intervals[idx][0] > end :
                res.append([start,end])
                start = intervals[idx][0]
                end = intervals[idx][1]
            else :
                end = max(intervals[idx][1],end)

            idx += 1

        res.append([start,end])
        return res
