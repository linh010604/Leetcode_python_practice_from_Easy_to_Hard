class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rpro = [1,nums[0]]
        pro = [1,nums[-1]]
        n = len(nums)

        for idx , num in enumerate(nums) :
            if idx > 0 :
                rpro.append(rpro[idx] * num)
                pro.append(pro[idx] * nums[n -1- idx])

        return [rpro[idx]*pro[n - idx - 1] for idx in range (n)]
