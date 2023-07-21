class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # set up for the array with first two element
        d = dict()
        d[0] = 1 
        if len(arr) >= 2 and arr[0] != arr[1]:
            d[1] = 2
        else :
            d[1] = 1
        
        res = max(d[0],d[1])
        
        # continue find the length the the subsequence end at index 'i' and find max when compared with d[i]
        for i in range (2,len(arr)) :
            if arr[i-2] > arr[i-1] :
                if arr[i] > arr[i-1] :
                    d[i] = d[i-1] + 1
                elif arr[i] < arr[i-1] :
                    d[i] = 2
                else :
                    d[i] = 1

            elif arr[i-2] < arr[i-1] :
                if arr[i] < arr[i-1] :
                    d[i] = d[i-1] + 1
                elif arr[i] > arr[i-1] :
                    d[i] = 2
                else :
                    d[i] = 1
            else :
                if arr[i] != arr[i-1] :
                    d[i] = d[i-1] + 1
                else :
                    d[i] = 1

            res = max(res,d[i])

        return res
