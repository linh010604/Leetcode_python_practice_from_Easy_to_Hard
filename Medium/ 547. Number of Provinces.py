def province( idx , map ,d) :
    dp = deque() 
    dp.append(idx)
    while len(dp) != 0 :
        tmp = dp.popleft()
        for i in range(len(map)) :
            if map[tmp][i] == 1 and d[i] == 0 :
                dp.append(i)
                d[i] = 1
    return 1
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        m = len(isConnected)
        d = list(0 for i in range(m))
        res = 0

        for i in range (m) :
            if d[i] == 0 :
                d[i] = 1
                res += province(i , isConnected , d)

        return res
