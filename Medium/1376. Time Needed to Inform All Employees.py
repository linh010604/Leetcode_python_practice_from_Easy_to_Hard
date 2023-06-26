class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        d = list(list() for i in range (n))
        res_list = list(0 for i in range (n))
        res = 0

        for i in range (n) :
            if i != headID :
                d[manager[i]].append(i)

        dp = deque()
        dp.append(headID) 

        while (len(dp) != 0) :
            tmp = dp.popleft()
            for i in range (len(d[tmp])) :
                dp.append(d[tmp][i])
                res_list[d[tmp][i]] = res_list[tmp] + informTime[tmp]
                res = max(res,res_list[d[tmp][i]])

        return res
