from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """ Do not return anything, modify matrix in-place instead.  """
        n = len(matrix)
        if n <= 1:
            return
        # transpose the matrix (flip across diagonal)
        for i in range(n):
            for j in range(i+1, n):
                if i != j:
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp

        # swap each row left/right, up to the middle element
        for i in range(n):
            for j in range(n // 2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][n-j-1]
                matrix[i][n-j-1] = temp



matrix = [
           [[1,2,3],[4,5,6],[7,8,9]],
           [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]],
           [[1]],
           [[1,2],[3,4]],
         ]

test_results = [
                [[7,4,1],[8,5,2],[9,6,3]],
                [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]],
                [[1]],
                [[3,1],[4,2]],
               ]
test_cases = len(test_results)

def run_test() -> None:
    sol = Solution()
    for i in range (test_cases):
        sol.rotate(matrix[i])
        test_flag = True if matrix[i] == test_results[i] else False
        if test_flag == True:
            print(f'++++ TEST #{i+1}: SUCCESS. Result = {matrix[i]}')
        else:
            print(f'---- TEST #{i+1}: FAILURE.')
            print(f'       Expected: {test_results[i]}')
            print(f'       Received: {matrix[i]}')

def main() -> None:
    run_test()

if __name__ == '__main__':
    main()
