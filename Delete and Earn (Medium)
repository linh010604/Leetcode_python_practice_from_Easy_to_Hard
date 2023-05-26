# dynamic programming
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        id1 = 0
        id2 = 0
        res = nums[0]
        nums.sort()

        d = [0] * (10**4+1)
        d[nums[0]] = nums[0]

        for i in range (1,len(nums)) :
            if nums[i] == nums[i-1] :
                d[nums[i]] += nums[i]
            else :
                d[nums[i]] += nums[i]
                if nums[i-1] + 1 < nums[i] :
                    d[nums[i]] += max(d[nums[i-1]],d[id1],d[id2])
                else :
                    d[nums[i]] += max(d[id1],d[id2])
                id2 = id1
                id1 = nums[i-1]
            res = max(res,d[nums[i]])
        
        print(d)
        return res
