from collections import defaultdict
class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        d = dict()

        for i , num in enumerate(arr) :
            d[arr[i]] = d.get(arr[i] - difference , 0) + 1

        return max(d.values())
