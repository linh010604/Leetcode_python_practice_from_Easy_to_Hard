class Solution(object):
    def maxValue(self, n, idx, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """
        l = 0
        r = maxSum
        res = 0

        while l <= r :
    
            mid = (l+r)/2
            if mid > idx :
                total = ( 2*mid - idx )*( idx + 1) / 2 
            else :
                total = mid * (mid + 1) /2 + idx - mid + 1 
            
            if mid > n - idx - 1:
                total += ( 2*mid - n + idx + 1 ) * ( n - idx ) / 2 - mid
            else :
                total += mid * (mid + 1) /2 + n - idx - 2*mid
            
            if total <= maxSum :
                l = mid + 1
                res = mid 
            else :
                r = mid - 1
                res = mid -1 

        return max(res,1)
