class Solution(object):
    def distanceTraveled(self, mainTank, additionalTank):
        """
        :type mainTank: int
        :type additionalTank: int
        :rtype: int
        """
        res = 0 
        while mainTank > 0 :
            if mainTank >= 5 :
                mainTank -= 5 
                if additionalTank >= 1 :
                    additionalTank -= 1
                    mainTank += 1
                    
                res += 5*10
            else :
                res += mainTank* 10
                mainTank = 0
                
        return res
        
