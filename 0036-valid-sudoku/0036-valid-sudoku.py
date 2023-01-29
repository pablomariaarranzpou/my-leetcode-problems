class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != "." and not self.valid(board, i, j, str(board[i][j])):
                    return False
        return True
    

    def valid(self, board, x, y, value):

        print(value)

        for j in range(len(board)):
            if(board[x][j] == value and j != y):
                print(x, y)
                return False
            if(board[j][y] == value and x != j):
                print(x, y)
                return False
        
        startx = (x//3)*3
        starty = (y//3)*3
        
        for j in range(startx, startx+3):
            for k in range(starty, starty+3):
                if(board[j][k] == value and x != j and y != k):
                    print(x, y)
                    return False
        
        return True

    