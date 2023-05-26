class Solution(object):
    def longestObstacleCourseAtEachPosition(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: List[int]
        """
        res = list ()
        ans = list()
        length = 0

        for idx in range(len(obstacles)) :
            res.append(0)

        for idx , item in enumerate(obstacles) :
            left = 0 
            right = length

            while left < right :
                mid = int((left + right) / 2)
                if res[mid] > obstacles[idx] :
                    right = mid 
                else :
                    left = mid + 1

            ans.append(left + 1)

            if left == length :
                length += 1

            res[left] = obstacles[idx]

        return ans
