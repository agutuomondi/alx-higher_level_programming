import sys

class NQueensSolver:
    def __init__(self, n):
        self.board = [[' ' for _ in range(n)] for _ in range(n)]
        self.solutions = []

    def deepcopy_board(self):
        return [row.copy() for row in self.board]

    def get_solution(self):
        return [[r, c] for r, row in enumerate(self.board) for c, value in enumerate(row) if value == "Q"]

    def xout(self, row, col):
        n = len(self.board)
        for c in range(col + 1, n):
            self.board[row][c] = "x"
        for c in range(col - 1, -1, -1):
            self.board[row][c] = "x"
        for r in range(row + 1, n):
            self.board[r][col] = "x"
        for r in range(row - 1, -1, -1):
            self.board[r][col] = "x"
        c = col + 1
        for r in range(row + 1, n):
            if c >= n:
                break
            self.board[r][c] = "x"
            c += 1
        c = col - 1
        for r in range(row - 1, -1, -1):
            if c < 0:
                break
            self.board[r][c]
            c -= 1
        c = col + 1
        for r in range(row - 1, -1, -1):
            if c >= n:
                break
            self.board[r][c] = "x"
            c += 1
        c = col - 1
        for r in range(row + 1, n):
            if c < 0:
                break
            self.board[r][c] = "x"
            c -= 1

    def recursive_solve(self, row, queens):
        n = len(self.board)
        if queens == n:
            self.solutions.append(self.get_solution())
            return

        for c in range(n):
            if self.board[row][c] == " ":
                tmp_board = self.deepcopy_board()
                tmp_board[row][c] = "Q"
                self.xout(row, c)
                self.recursive_solve(row + 1, queens + 1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit() or int(sys.argv[1]) < 4:
        print("N must be an integer greater than or equal to 4")
        sys.exit(1)

    n_queens_solver = NQueensSolver(int(sys.argv[1]))
    n_queens_solver.recursive_solve(0, 0)

    for sol in n_queens_solver.solutions:
        print(sol)
