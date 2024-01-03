class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        print(bank[0].count('0'))

        previous = bank[0].count('1')
        res = 0

        for i in range (1, len(bank)):
            if bank[i].count('1') != 0 :
                tmp = bank[i].count('1')
                res += previous * tmp
                previous = tmp


        return res
        
