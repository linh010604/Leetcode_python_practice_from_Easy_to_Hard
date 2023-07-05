class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """

        if s == goal :
            if len(set(s)) == len(s) :
                return False
            else:
                return True
        else:
            if len(s) != len(goal) :
                return False
            else :
                cnt = 0 
                pre = -1
                for idx in range(len(s)) :
                    if s[idx] != goal[idx] :
                        cnt += 1
                    
                        if pre == -1 :
                            pre = idx
                        else :
                            if s[idx] != goal[pre] or goal[idx] != s[pre]:
                                return False

                    if cnt > 2 :
                        return False

                if cnt < 2 :
                    return False
                return True
