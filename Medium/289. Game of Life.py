R = [-1, 0, 1, 0, -1, 1, -1, 1]
C = [0, 1, 0, -1, -1, 1, 1,-1]
def check(checkboard, board, x, y) :
    die = live  = 0
    for i in range(8) :
        if 0 <= x + R[i] < len(checkboard) and 0 <= y + C[i] < len(checkboard[0]) :
            if checkboard[x+R[i]][y+C[i]] == 0:
                die += 1
            else :
                live += 1


    if board[x][y] == 0 and live == 3 :
        board[x][y] = 1

    if board[x][y] == 1 :
        if live < 2 or live > 3:
            board[x][y] = 0
        elif live == 2 or live == 3 :
            board[x][y] = 1

    
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        checkboard = deepcopy(board)
        
        m = len(board)
        n = len(board[0])

        for i in range (m) :
            for j in range (n) :
                check(checkboard, board, i , j)
