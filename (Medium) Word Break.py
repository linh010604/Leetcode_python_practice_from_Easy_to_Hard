class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        d = list(0 for i in range(len(s) + 1))
        d[0] = 1
        for idx , letter in enumerate(s) :
            for word in wordDict :
                #print (idx , word, idx - len(word)+1)
                if idx >= len(word)-1 and word == s[idx - len(word)+1:idx+1] and d[idx - len(word)+1] == 1:
                    d[idx + 1] = 1
                    break
        res = 0
        if d[-1] == 1 :
            return True
        return False
        
