class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()

        len_nums = len(nums)

        if len_nums % 2 == 0 :
            total = (nums[len_nums/2] + nums[len_nums/2-1])
            if total % 2 == 0 :
                return total/2
            else :
                return total/2 + 0.5
        else :
            return nums[len_nums//2]
