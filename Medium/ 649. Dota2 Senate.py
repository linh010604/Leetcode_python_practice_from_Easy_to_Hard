class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        len_s = len(senate)
        str_R = deque()
        str_D = deque()
        for idx in range (len_s) :
            if senate[idx] == 'R' :
                str_R.append(idx)
            else :
                str_D.append(idx)
                
        while len(str_D) and len(str_R) :
            D = str_D.popleft()
            R = str_R.popleft()
            if D > R :
                str_R.append(R+len_s)
            else :
                str_D.append(D+len_s)
        if len(str_R):
            return "Radiant"
        else :
            return "Dire"
