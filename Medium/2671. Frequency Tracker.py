class FrequencyTracker(object):

    def __init__(self):
        self.d = {}
        self.fre = {}
             
    def add(self, number):
        """
        :type number: int
        :rtype: None
        """

        cnt = self.d.get(number,0)
        self.d[number] = cnt + 1
        self.fre[cnt+1] = self.fre.get(cnt+1,0) + 1
        self.fre[cnt] = self.fre.get(cnt,1) - 1

    def deleteOne(self, number):
        """
        :type number: int
        :rtype: None
        """
        if self.d.get(number,0) != 0:
            self.fre[self.d[number]] -= 1
            self.d[number] -= 1
            if self.d[number] != 0 :
                self.fre[self.d[number]] += 1
        
    def hasFrequency(self, frequency):
        """
        :type frequency: int
        :rtype: bool
        """
        if self.fre.get(frequency,0) != 0:
            return True
        return False
