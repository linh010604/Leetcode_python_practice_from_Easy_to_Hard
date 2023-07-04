def generate(n , k , d , res , idx , cnt) :
    if cnt == k :
        res.append(deepcopy(d))
    else :
        for i in range (idx + 1 , n + 2 - (k - cnt)) :
            d.append(i)
            generate(n , k , d , res , i , cnt + 1)
            d.pop()

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        d = []
        res = []
        for i in range (1 , n + 2 - k) :
            d.append(i)
            generate(n,k,d,res , i , 1 )
            d.pop()

        return res
