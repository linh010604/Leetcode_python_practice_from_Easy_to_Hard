class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """

        res = 0

        for item in hours :
            if item >= target:
                res += 1

        return res
