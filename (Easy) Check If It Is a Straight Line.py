class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if coordinates[-1][0]-coordinates[0][0] != 0 :

            slope = float(coordinates[-1][1]-coordinates[0][1])/(coordinates[-1][0]-coordinates[0][0]) 

            for i in range (1,len(coordinates)) :
                try :
                    if float(coordinates[0][1]-coordinates[i][1])/(coordinates[0][0]-coordinates[i][0]) != slope :
                        return False
                except :
                    return False
        else :
            for i in range (1,len(coordinates)) :
                if coordinates[i][0] != coordinates[0][0] :
                    return False
        return True
