class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0

        for i in range(len(points)):
            d = dict()
            for j in range (i + 1 , len(points)):
                if points[i][0] == points[j][0] :
                    a = 0
                    b = 1
                else :
                    a = float(points[i][1] - points[j][1])/(points[i][0] - points[j][0])
                    b = points[i][1] - a*points[i][0]
                d[(a,b)] = d.get((a,b) , 0) + 1
                res = max(res,d[(a,b)])

        return res + 1
