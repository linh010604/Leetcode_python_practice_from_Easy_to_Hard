class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for idx, item in enumerate(numbers) :
            d[item] = idx
        for idx, item in enumerate(numbers) :
            try : 
                return [idx+1,d[target - item]+1]
            except :
                pass
