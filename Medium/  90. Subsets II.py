import copy
def make_sub(nums , res , d , start) :
    if start < len(nums) :
        for i in range (start , len(nums)) :
            d.append(nums[i])
            res.add(tuple(d))
            make_sub(nums , res , d , i + 1)
            d.pop()
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = set()

        nums.sort()

        res.add(())

        make_sub(nums , res , [] , 0)

        return list(res)
