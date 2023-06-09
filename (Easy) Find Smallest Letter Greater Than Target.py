class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left = 0
        right = len(letters)-1
        res = 0

        while left <= right :
            mid = int((left + right) / 2)
            if letters[mid] <= target :
                left = mid + 1
                res = mid + 1
            else :
                right = mid - 1
                res = mid

        if res > len(letters) - 1 :
            return letters[0]

        return letters[res]
