class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        max_tmp = 0
        d = dict()
        for item in nums :
            d[item] = d.get(item,0) + 1
            max_tmp = max(max_tmp ,  d[item])
        
        dd = list()
        for i in range (max_tmp):
            dd.append([])

        #print (max_tmp, dd)

        for key in d.keys() :
            while d[key] > 0 :
                d[key] -= 1
                dd[d[key]].append(key)
                

        return dd
        
