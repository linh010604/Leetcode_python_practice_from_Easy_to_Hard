class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 2 :
            return nums
        
        d = dict()
        for item in nums:
            d[item] = d.get(item,0) + 1

        return [item for item in d.keys() if d[item] == 1]
