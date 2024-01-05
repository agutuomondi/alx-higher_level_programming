import sys


class NQueensSolver:
    def __init__(self, n):
        if not isinstance(n, int) or n < 4:
            raise ValueError("N must be an integer greater than or equal to 4")
        self.n = n
        self.board = [[' ' for _ in range(n)] for _ in range(n)]
        self.solutions = []

    def solve(self):
        self.recursive_solve(0, 0)
        return self.solutions

    def recursive_solve(self, row, queens):
        if queens == self.n:
            self.solutions.append(self.get_solution())
            return

        for col in range(self.n):
            if self.board[row][col] == ' ':
                tmp_board = [row.copy() for row in self.board]
                tmp_board[row][col] = 'Q'
                self.xout(tmp_board, row, col)
                self.recursive_solve(row + 1, queens + 1)

    def get_solution(self):
        return [[row, col] for row in range(self.n) for col in range(self.n) if self.board[row][col] == 'Q']

    def xout(self, board, row, col):
        for c in range(col + 1, self.n):
            board[row][c] = 'x'
        for c in range(col - 1, -1, -1):
            board[row][c] = 'x'
        for r in range(row + 1, self.n):
            board[r][col] = 'x'
        for r in range(row - 1, -1, -1):
            board[r][col] = 'x'
        c = col + 1
        for r in range(row + 1, self.n):
            if c >= self.n:
                break
            board[r][c] = 'x'
            c += 1
        c = col - 1
        for r in range(row - 1, -1, -1):
            if c < 0:
                break
            board[r][c] = 'x'
            c -= 1
        c = col + 1
        for r in range(row - 1, -1, -1):
            if c >= self.n:
                break
            board[r][c] = 'x'
            c += 1
        c = col - 1
        for r in range(row + 1, self.n):
            if c < 0:
                break
            board[r][c] = 'x'
            c -= 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
        solver = NQueensSolver(n)
        solutions = solver.solve()
        for sol in solutions:
            print(sol)
    except ValueError as e:
        print(e)
        sys.exit(1)
