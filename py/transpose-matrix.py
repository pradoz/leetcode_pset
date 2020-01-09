# Time+space complexity are both O(m * n), where m is the number of rows in the
# matrix, and n is the number of columns in the matrix.
class Solution0:
    def transpose(self, matrix: [[int]]) -> [[int]]:
        if len(matrix) == 0:
            return []

        # construct equivalent dimension matrix of all zeroes
        result = [[0] * len(matrix) for _ in range(len(matrix[0]))]

        for i, row in enumerate(matrix):
            for j, entry in enumerate(row):
                result[j][i] = entry

        return result


class Solution:
    def transpose(self, matrix: [[int]]) -> [[int]]:
        return list(zip(*matrix))



print(Solution().transpose([[1,2,3],\
                            [4,5,6],\
                            [7,8,9]])) # [[1,4,7],[2,5,8],[3,6,9]]