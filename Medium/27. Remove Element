class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        s = " "

        for item in nums :
            s +=  " " + str(item) + " "

        s = s.replace(" "+str(val)+" ",' _ ')

        s = s[1:-1]

        s = s.split("  ")

        cnt = 0

        for i in range (len(nums)):
            try:
                nums[i] = int(s[i])
                cnt += 1
            except :
                nums[i] = s[i]

        nums.sort()

        return cnt
