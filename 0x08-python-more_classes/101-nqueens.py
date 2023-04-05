#!/usr/bin/python3
"""N×N chessboard"""


class NQueens:
    """Positioning queens"""
    def find_solutions(self, n):
        col = set()
        pos_diag = set()
        neg_diag = set()
        solutions = []
        board = [['.'] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                solutions.append(copy)
                return

            for c in range(n):
                if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return solutions


def get_queen_positions(solutions):
    """Finding positions"""
    queen_positions = []
    for solution in solutions:
        positions = []
        for i in range(len(solution)):
            for j in range(len(solution)):
                if solution[i][j] == 'Q':
                    positions.append([i, j])
        queen_positions.append(positions)
    return queen_positions


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    n = int(sys.argv[1])
    nqueens = NQueens()
    solutions = nqueens.find_solutions(n)
    queen_positions = get_queen_positions(solutions)
    for i in queen_positions:
        print(i)
