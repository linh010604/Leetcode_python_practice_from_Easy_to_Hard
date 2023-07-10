class Solution(object):
    def maxNonDecreasingLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        d1 = list(1 for i in range(len(nums1)))
        d2 = list(1 for i in range(len(nums1)))
        
        for i in range (1 , len(nums1)) :
            if nums1[i] >= nums2[i-1] :
                d1[i] = max(d1[i],d2[i-1] + 1)
            if nums1[i] >= nums1[i-1] :
                d1[i] = max(d1[i],d1[i-1] + 1)
                
            if nums2[i] >= nums2[i-1] :
                d2[i] = max(d2[i],d2[i-1] + 1)
            if nums2[i] >= nums1[i-1] :
                d2[i] = max(d2[i],d1[i-1] + 1)
                
        print(d1 , d2)
                
        return max(max(d1),max(d2))
        
