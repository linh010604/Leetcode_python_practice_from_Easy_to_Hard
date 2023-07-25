class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        l = 0
        r= len(arr) - 1
        res = 0

        while l <= r :

            mid = (l+r) / 2

            if arr[mid-1] < arr[mid] > arr[mid + 1] :
                return mid
            elif mid > 0 and arr[mid] < arr[mid-1] :
                res = r = mid - 1
            else :
                res = l = mid + 1


        return res
