class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """

        d = dict()
        n = len(words)

        for word in words:
            for letter in word:
                d[letter] = d.get(letter,0) + 1 

        for k in d.keys() :
            if d[k] % n != 0 :
                return False

        return True
        
