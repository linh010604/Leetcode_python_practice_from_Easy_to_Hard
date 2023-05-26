def get_max(idx , questions , d) :
        if idx >= len(questions) :
            return 0
        if d.get(idx,-1) != -1 :
            return d[idx]
         
        take_it = questions[idx][0] + get_max(idx + questions[idx][1] + 1 , questions , d)
        leave_it = get_max(idx + 1 , questions , d)

        d[idx] = max(take_it , leave_it)

        return d[idx]

class Solution(object):

    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        d = dict()
        
        return get_max(0,questions,d)

