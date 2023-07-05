class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        current_height = height[0]
        volume = 0
        res = 0
        
        for i , water in enumerate (height) :
            
            if height[i] < current_height :
                volume += current_height - height[i]
            else :
                current_height = height[i]
                res += volume
                volume = 0

        current_height = height[-1]
        volume = 0

        for i in range (len(height) - 1 , -1 , -1) :
            if height[i] < current_height :
                volume += current_height - height[i]
            elif height[i] > current_height :
                current_height = height[i]
                res += volume
                volume = 0

        return res
