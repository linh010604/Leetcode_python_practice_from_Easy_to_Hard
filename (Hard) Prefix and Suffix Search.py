class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.check = dict()

        for i in range (len(words)) :
            word = words[i]
            wlen = len(word)
            for j in  range (wlen) :
                for k in range (wlen) :
                    pref = word[:j+1]
                    suff = word[k:]
                    self.check[pref + "|" + suff] = i

    def f(self, pref, suff):
        """
        :type pref: str
        :type suff: str
        :rtype: int
        """
        return self.check.get(pref + "|" + suff , -1)
        
