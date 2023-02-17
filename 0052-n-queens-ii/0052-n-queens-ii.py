class Solution:

    def __init__(self):
        self.sols = []
        self.count = 0

    def totalNQueens(self, n: int) -> List[List[str]]:
        
        board = ["."*n for _ in range(n)] 
        self.solve_queens_backtracking(n, board, 0)
        return self.count
    
    def solve_queens_backtracking(self, N, board, col):
        
        if(col == N):
            self.sols.append(board.copy())
            self.count += 1
       
        for i in range(N):
            
            if (self.check_position_previous_columns(board, i, col)):
                board[i] = board[i][:col] + 'Q' + board[i][col + 1:]
                
                if self.solve_queens_backtracking(N, board, col + 1):
                    return board
            
                board[i] = board[i][:col] + '.' + board[i][col + 1:]
            
        return False

    def check_position_previous_columns(self, board, row, col):
    
        # Comprovem les columnes anteriors de la fila 'row'
        for i in range(col):
            if board[row][i] == 'Q':
                return False

        # Comprovem la diagonal inferior
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        # Comprovem la diagonal superior
        for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        return True