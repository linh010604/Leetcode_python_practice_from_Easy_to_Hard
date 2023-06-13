class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums_list = list()

        ok = True

        for i in range(0,len(nums)-1) :
            if nums[i] < nums[i+1] :
                index = i
                ok = False
        if ok :
            for i in range (0 , len(nums)//2) :
                x = nums[i]
                nums[i] = nums[len(nums) - 1 - i]
                nums[len(nums) - 1 - i] = x
        else :
            print(index)
            for i in range(len(nums)-1,index,-1) :
                if nums[i] > nums[index] :
                    x = nums[index]
                    nums[index] = nums[i]
                    nums[i] = x
                    break
            print(nums)
            r=0
            for i in range(index+1,index+(len(nums)-index)//2+1) :
                print(i,len(nums)-r+1)
                r += 1
                x = nums[min(len(nums)-r,len(nums)-1)]
                nums[min(len(nums)-r,len(nums)-1)] = nums[i]
                nums[i] = x    
        return nums
