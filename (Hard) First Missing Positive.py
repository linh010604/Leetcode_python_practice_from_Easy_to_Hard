class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        d = dict()

        for idx , item in enumerate(nums) :
            if item > 0 :
                d[item] = 1 
        i = 1
        while 1 :
            if d.get(i,0) == 1 :
                i += 1
            else :
                return i
