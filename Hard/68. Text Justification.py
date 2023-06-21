class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        start = 0
        end = 0
        s = []

        while start < len(words) :
    
            res = ""
            total = 0
            while end < len(words) and total + len( words[end] ) + 1 <= maxWidth + 1:
                
                total += len( words[end] ) + 1
                end += 1

            total -=  1

            if end - 1 == start :
                res += words[start] + (maxWidth - len(words[start]) ) *" "
                start = end
                s.append(res)
                continue

            blank = (maxWidth - total)/(end - start - 1)
            more = (maxWidth - total)%(end - start - 1)
            idx = 0

            res += words[start]

            if end == len(words) :
                for i in range ( start + 1 , end) :
                    res += " " 
                    res += words[i]
                res += (maxWidth - total) * " "
            else :
                for i in range ( start + 1 , end) :
                    if idx < more :
                        res += " " + (blank + 1) * " "
                        idx += 1
                    else :
                        res += " " + blank * " "
                    res += words[i]
            start = end 
            
            s.append(res)

        return s
