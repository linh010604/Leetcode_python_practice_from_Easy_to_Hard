def generate(res,_list,nums,idx) :
    for i in range (idx , len(nums)) :
        _list.append(nums[i])
        res.append(deepcopy(_list))
        generate(res , _list , nums , i + 1)
        _list.pop()
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        generate(res,[],nums,0)
        return res
