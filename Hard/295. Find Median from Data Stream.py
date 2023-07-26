class MedianFinder(object):

    def __init__(self):
        self.fin = list()
        self.len = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.fin.append(num)
        self.len += 1

    def findMedian(self):
        """
        :rtype: float
        """
        self.fin.sort()
        if self.len % 2 == 1 :
            return self.fin[self.len/2]
        return (self.fin[self.len/2-1] + self.fin[self.len/2]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
