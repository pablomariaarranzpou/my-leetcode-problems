class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.solveSudkuBacktracking(board)

    def nextEmpty(self, board):

        for i in range(len(board)):
            for j in range(len(board)):
                if(self.board[i][j] == '.'):
                    return i, j
        return -1, -1    

    def solveSudkuBacktracking(self, board):

        x, y = self.nextEmpty(board)

        if x == -1 and y == -1:
            return True

        for i in range(1, 10):

            if(self.satisfies(board, x, y, i)):
                
                self.board[x][y] = str(i)

                if self.solveSudkuBacktracking(board):
                    return True
                
                self.board[x][y] = '.'
    
        return False


    def satisfies(self, board, x, y, value):

        for j in range(len(board)):
            if(board[x][j] == str(value)):
                return False
        
        for j in range(len(board)):
            if(board[j][y] == str(value)):
                return False
        
        startx = (x//3)*3
        starty = (y//3)*3
        
        for j in range(startx, startx+3):
            for k in range(starty, starty+3):
                if(board[j][k] == str(value)):
                    return False
        
        return True

    



