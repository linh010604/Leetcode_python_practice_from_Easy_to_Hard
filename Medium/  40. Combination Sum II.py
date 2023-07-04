def check(candidates , target , total , alist , res , idx) :
    if total == target :
        a = deepcopy(alist)
        a.sort()
        if a not in res :
            res.append(a)
    else :
        for i in range (idx, len(candidates)) :
            if total + candidates[i] <= target and ((candidates[i] != candidates[i-1] and i > idx) or i == idx ):
                alist.append(candidates[i])
                check(candidates , target , total + candidates[i] , alist , res , i + 1)
                alist.pop()

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = list()
        candidates.sort()

        check (candidates , target , 0 , [] , res , 0)

        return res
