class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for idx , item in enumerate(strs[0]) :
            for itm in strs :
                if idx >= len(itm) or itm[idx] != item :
                    return res
            res += item

        return res
