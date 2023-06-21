# using deque to append the position of character '(', and then
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        d = deque()
        d.append(-1)
        idx = 0
        res = 0
        kq = 0

        if len(s) <= 0 :
            return 0

        while idx < len(s) :
            if s[idx] == ')':
                d.pop()
                if len(d) > 0 :
                    res = idx - d[-1]
                    kq = max(kq,res)
                else :
                    d.append(idx)

            else :
                d.append(idx)

            idx += 1

        return kq
