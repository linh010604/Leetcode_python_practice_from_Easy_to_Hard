def check (ok , board , word , row , col , idx) :
    #print (row , col , idx)
    if idx == len(word) :
        return True

    if row + 1 < len(board) and ok[row + 1][col] == True and board[row+1][col] == word[idx] :
        ok[row+1][col] = False
        #print(row)
        if check(ok , board , word , row + 1 , col , idx + 1) :
            return True
        ok[row + 1][col] = True

    if row - 1 > -1 and ok[row - 1][col] == True and board[row - 1][col] == word[idx] :
        ok[row - 1][col] = False
        #print(row)
        if check(ok  ,board , word , row  -  1 , col , idx + 1):
            return True
        ok[row -  1][col] = True

    if col + 1 < len(board[0]) and ok[row][col + 1] == True and board[row][col+1] == word[idx] :
        ok[row][col+1] = False
        #print(row)
        if check(ok , board , word , row , col + 1 , idx + 1) :
            return True
        ok[row][col + 1] = True

    if col - 1 > -1 and ok[row][col - 1] == True and board[row][col-1] == word[idx] :
        ok[row][col - 1] = False
        #print(row)
        if check(ok , board , word , row , col - 1 , idx + 1) :
            return True
        ok[row][col - 1] = True

    return False
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        m = len(board)
        n = len(board[0])
        ok = list()

        for i in range (m) :
            ok.append(list())
            for j in range (n) :
                ok[i].append(True)

        for i in range (m) :
            for j in range (n) :
                if board[i][j] == word[0] :
                    ok[i][j] = False
                    if check(ok , board , word , i , j , 1) == True :
                        return True 
                    ok[i][j] = True

        return False
