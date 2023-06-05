# Using dynamic programming to know the longest common subarray end with ith position in array nums1 
# and jth position in array nums2

class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        d = list()
        res = 0
        for idx in range(len(nums1)+1) :
            d.append(list())
            for idex in range(len(nums2)+1) :
                d[idx].append(0)

        for i in range(len(nums1)) :
            for j in range(len(nums2)) :
                if nums1[i] == nums2[j] :
                    d[i+1][j+1] = d[i][j] + 1
                res = max(res,d[i+1][j+1])

        #print(d)
        return res
