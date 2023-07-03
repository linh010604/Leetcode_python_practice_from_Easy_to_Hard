def get(check , idx , res , digits , current) :
    if idx == len(digits) :
        res.append(current)
    else :
        for i in range( len( check[ int( digits[idx] ) ] ) ) :
            current += check[ int( digits[idx] ) ][i]
            get(check , idx + 1 , res , digits , current)
            current = current[:-1]
    return res

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "" :
            return []

        check = ["" , "" , 'abc' , 'def' , 'ghi', 'jkl' , 'mno' , 'pqrs' , 'tuv' , 'wxyz']
        res = list()

        return get(check , 0 , res , digits , "")
