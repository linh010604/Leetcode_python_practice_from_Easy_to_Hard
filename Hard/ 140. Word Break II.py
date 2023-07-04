class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        d = list(0 for i in range(len(s) + 1))
        d[0] = 1

        res = list(list() for i in range(len(s) + 1))
        res[0].append("")
        for idx , letter in enumerate(s) :
            for word in wordDict :
                if idx >= len(word)-1 and word == s[idx - len(word)+1:idx+1] and d[idx - len(word)+1] >= 1:
                    
                    if idx + 1 < len(s) :
                        for item in res[idx - len(word)+1] :
                            res[idx + 1] .append( item + word + ' ')
                    else :
                        for item in res[idx - len(word)+1] :
                            res[idx + 1] .append( item + word)
                    d[idx + 1] += d[idx - len(word)+1]
        
        return res[-1]
