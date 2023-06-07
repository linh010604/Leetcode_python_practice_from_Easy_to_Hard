import copy
class Solution(object):
    def permuteUnique(self, s):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        list_= list()
        amount = 1
        list_.append(s)
        for i in range (1,len(s)+1):
            amount *= i 
            
        for i in range (amount-1) :
            nums = copy.deepcopy(list_[i])
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
                    #print(index)
                    for i in range(len(nums)-1,index,-1) :
                        if nums[i] > nums[index] :
                            x = nums[index]
                            nums[index] = nums[i]
                            nums[i] = x
                            break
                    #print(nums)
                    r=0
                    #nums[index+1 : index+(len(nums)-index)//2+1].sort()
                    for i in range(index+1,index+(len(nums)-index)//2+1) :
                        print(i,len(nums)-r+1)
                        r += 1
                        x = nums[min(len(nums)-r,len(nums)-1)]
                        nums[min(len(nums)-r,len(nums)-1)] = nums[i]
                        nums[i] = x 

            if nums not in list_:
                list_.append(nums)
            else :
                break 
     
        return (list_)

