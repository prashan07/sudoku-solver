class Solution:
    def solveSudoku(self, board):
        if board is None or len(board) == 0:
            return
        self.solve(board)
        print(board)

    def solve(self, board):
        mynums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    for num in mynums:
                        if(self.isValid(board, i, j, num)):
                            board[i][j] = num

                            if(self.solve(board)):
                                return True
                            else:
                                board[i][j] = "."

                    return False
        return True

    def isValid(self, board, row, col, num):
        for i in range(9):
            if board[i][col] == num:
                return False
            if board[row][i] == num:
                return False
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                return False
        return True


myboard = Solution()
# board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
board = [[".", ".", ".", "2", "6", ".", "7", ".", "1"], ["6", "8", ".", ".", "7", ".", ".", "9", "."], ["1", "9", ".", ".", ".", "4", "5", ".", "."], ["8", "2", ".", "1", ".", ".", ".", "4", "."], [".", ".", "4", "6",
                                                                                                                                                                                                      ".", "2", "9", ".", "."], [".", "5", ".", ".", ".", "3", ".", "2", "8"], [".", ".", "9", "3", ".", ".", ".", "7", "4"], [".", "4", ".", ".", "5", ".", ".", "3", "6"], ["7", ".", "3", ".", "1", "8", ".", ".", "."]]
myboard.solveSudoku(board)
