class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """

        res = list()
        res.append(0) 

        for idx, item in enumerate (gain) :
            res.append(res[idx] + gain[idx])
            
        return max(res)
            
