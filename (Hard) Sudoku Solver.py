def check(board, x, y, k) :
    for i in range(9) :
        if (board[i][y] == k) or (board[x][i]) == k :
            return False
    a = x // 3
    b = y // 3

    for i in range (3*a,3*a+3) :
        for j in range(3*b, 3*b + 3) :
            if board[i][j] == k :
                return False

    return True

def solve (board , x , y) :
    if y == 9 :
        if x == 8 :
            return True
        else :
            if solve(board , x + 1, 0):
                return True
    elif  board[x][y] == '.' :
        for i in range(1,10) :
            if check(board, x, y, str(i)) :
                board[x][y] = str(i)
                if solve(board , x , y+1) :
                    return True
                board[x][y] = '.'
    else :
        if solve(board, x, y + 1) :
            return True

    return False

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        for x in range (9) :
            for y in range(9) :
                if board[x][y] == '.' :
                    solve(board , x , y)
                    return 0

        

