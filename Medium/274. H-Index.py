class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        citations.sort()

        res = 0 

        idx = len(citations) - 1

        while idx >= 0:
            res = max(res, min(len(citations) - idx, citations[idx]))
            idx -= 1

        return res
