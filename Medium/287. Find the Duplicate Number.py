class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict()

        for item in nums :
            d[item] = d.get(item,0) + 1
            if d[item] == 2 :
                return item
