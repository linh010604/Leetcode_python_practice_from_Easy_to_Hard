class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = dict()
        res = 1
        kq = 0

        d = list(1 for i in range(len(nums)))
        cnt = list(1 for i in range(len(nums)))
        cnt[0] = 1

        for i in range (len(nums)) :
            for j in range(i) :
                if nums[j] < nums[i] :
                    if d[i] < d[j] + 1 :
                        cnt[i] = cnt[j]
                    elif d[i] == d[j] + 1:
                        cnt[i] += cnt[j]
                    
                    d[i] = max(d[i] , d[j] + 1)
            if d[i] > res :
                kq = cnt[i]
            elif d[i] == res :
                kq += cnt[i]
            res = max(res, d[i])

        return kq
