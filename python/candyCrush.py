class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        """
        his question is about implementing a basic elimination algorithm for Candy Crush.

Given a 2D integer array board representing the grid of candy, different positive integers board[i][j] represent different types of candies. A value of board[i][j] = 0 represents that the cell at position (i, j) is empty. The given board represents the state of the game following the player's move. Now, you need to restore the board to a stable state by crushing candies according to the following rules:

If three or more candies of the same type are adjacent vertically or horizontally, "crush" them all at the same time - these positions become empty.
After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these candies will drop until they hit a candy or bottom at the same time. (No new candies will drop outside the top boundary.)
After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
If there does not exist more candies that can be crushed (ie. the board is stable), then return the current board.
You need to perform the above rules until the board becomes stable, then return the current board.
        """
        
        def iscrushable(board):
            crushable=False
            for i in range(m):
                for j in range(n):
                    if i<m-2 and abs(board[i][j])==abs(board[i+1][j])==abs(board[i+2][j])!=0:
                        board[i][j]=-abs(board[i][j])
                        board[i+1][j]=-abs(board[i][j])
                        board[i+2][j]=-abs(board[i][j])
                        crushable=True
                    if j<n-2 and abs(board[i][j])==abs(board[i][j+1])==abs(board[i][j+2])!=0:
                        board[i][j]=-abs(board[i][j])
                        board[i][j+1]=-abs(board[i][j])
                        board[i][j+2]=-abs(board[i][j])
                        crushable=True
                    
            
            return crushable
        
        def crush(board):
                                   
            for j in range(n):
                nonzerorow = m-1
                for i in reversed(range(m)):
                    if board[i][j]<=0:
                        continue
                    else:
                        board[nonzerorow][j]=board[i][j]
                        nonzerorow -= 1
                for i in range(nonzerorow, -1,-1):
                    board[i][j]=0
            
            return board
        
        m,n = len(board), len(board[0])
        while iscrushable(board):
            board = crush(board)
        return board