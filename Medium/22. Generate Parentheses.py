def generate(dp , openn , close , n ,res) :

    if openn == close == n :
        res.append("".join(dp))
    else:
        if openn < n :
            dp.append('(')
            generate(dp , openn + 1 , close , n , res)
            dp.pop()
        if openn > close :
            dp.append(')')
            generate(dp , openn , close + 1 , n , res)
            dp.pop()

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        dp = list()
        res = list()

        generate(dp , 0 , 0 , n ,res)

        return res
