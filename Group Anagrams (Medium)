class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        new_strs = list()

        for idx , item in enumerate(strs) :
            new_strs.append([sorted(list(item)) , idx])

        new_strs.sort()

        check = new_strs[0][0]

        res = list()
        check_list = list()

        for idx , item in enumerate(new_strs) :
            if item[0] == check :
                check_list.append(strs[item[1]])
            else :
                res.append(check_list)
                check_list = [strs[item[1]]]
                check = item[0]

            if idx == len(strs) - 1 :
                res.append(check_list)

        return (res)
