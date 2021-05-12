from typing import List

# O(1) time for calls to sumRegion(...)
# O(M) = O(n^2) time to initialize
# O(M) space
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.matrix = None
        # dictionary representation of a matrix
        # self.matrix = {(i,j):0 for i in range(self.m) for j in range(self.n)}

        # precompute the sum at every rectangle ending at matrix(i,j)
        for i in range(self.n):
            for j in range(self.m):
                if i > 0 and j > 0:
                    matrix[i][j] -= matrix[i-1][j-1]
                if i > 0:
                    matrix[i][j] += matrix[i-1][j]
                if j > 0:
                    matrix[i][j] += matrix[i][j-1]
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.matrix[row2][col2]
        if row1 > 0 and col1 > 0:
            total += self.matrix[row1-1][col1-1]
        if row1 > 0:
            total -= self.matrix[row1-1][col2]
        if col1 > 0:
            total -= self.matrix[row2][col1-1]

        return total


# O(i * j) time
# O(M) space
class NumMatrix0:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                total += self.matrix[i][j]

        return total








def run_test() -> None:
    sol = NumMatrix([[3, 0, 1, 4, 2],
                     [5, 6, 3, 2, 1],
                     [1, 2, 0, 1, 5],
                     [4, 1, 0, 1, 7],
                     [1, 0, 3, 0, 5]])
    print(sol.sumRegion(2, 1, 4, 3)) # return 8 (i.e sum of the red rectangle)
    print(sol.sumRegion(1, 1, 2, 2)) # return 11 (i.e sum of the green rectangle)
    print(sol.sumRegion(1, 2, 2, 4)) # return 12 (i.e sum of the blue rectangle)


def main() -> None:
    run_test()

if __name__ == '__main__':
    main()
