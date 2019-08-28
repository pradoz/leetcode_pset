'''
Example:
Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
Output: 35
Explanation: 
The grid is:
[ [3, 0, 8, 4], 
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]

The skyline viewed from top or bottom is: [9, 4, 8, 7]
The skyline viewed from left or right is: [8, 7, 9, 3]

The grid after increasing the height of buildings without affecting skylines is:

gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]
'''

# Naive solution
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: [[int]]) -> int:
        columns = list(zip(*grid))

        left_right_skyline = []
        for row in grid:
            left_right_skyline.append(max(row))
        
        top_bot_skyline = []
        for row in columns:
            top_bot_skyline.append(max(row))

        total = 0
        for i, row in enumerate(left_right_skyline):
            for j, col in enumerate(top_bot_skyline):
                # max(row, col)
                if row > col:
                    total = total + col - grid[i][j] 
                else:
                    total = total + row - grid[i][j] 
        return total

# More pythonic solution
class Solution0:
    def maxIncreaseKeepingSkyline(self, grid: [[int]]) -> int:
        rows, cols = list(map(max, grid)), list(map(max, zip(*grid)))
        print(sum(min(i, j) for i in rows for j in cols))
        return sum(min(i, j) for i in rows for j in cols) - sum(map(sum, grid))

class Solution1:
    def maxIncreaseKeepingSkyline(self, grid: [[int]]) -> int:
        top_skyline = [max(row) for row in grid]
        side_skyline = [max(col) for col in zip(*grid)]

        total = 0
        for i, row in enumerate(grid):
            for j, height in enumerate(row):
                total += min(side_skyline[i], top_skyline[j]) - height
        return total

grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
print(Solution().maxIncreaseKeepingSkyline(grid))
