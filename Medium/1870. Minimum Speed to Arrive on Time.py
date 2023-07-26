class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        """
        :type dist: List[int]
        :type hour: float
        :rtype: int
        """

        if len(dist) > math.ceil(hour) :
            return -1

        r = 10E7
        l = 1
        res = 0

        while l <= r :
            mid = int((l+r)/2)

            total = 0 

            for i in range (len(dist) - 1):
                total += math.ceil(float(dist[i])/mid)

            total += float(dist[-1])/mid

            if total > hour :
                l = mid + 1
                res = mid + 1
            else :
                res = mid
                r = mid - 1

        return res
