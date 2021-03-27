


''' DFS - visit each cell and mark adjacent land '''
class SolutionDFS:
    def numIslands(self, grid) -> int:
        if not grid: return 0

        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    island_count += 1
        return island_count

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#' # mark as visited

        # call dfs on adjacent squares
        self.dfs(grid, i-1, j)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j-1)
        self.dfs(grid, i, j+1)



'''
Solution Explanation:
    Traverse the grid until we find a land block, then call DFS on any
    adjacent land blocks and mark them as "seen." Continue until we've called
    DFS for every land block.

If m and n are the number of rows and columns in the grid, respectively, then:
Time Complexity: O(m*n), since we may have to check every value in n for every
    value in m.
Space Complexity: O(m*n), in the worst case of all land blocks, we have to
    store the entire grid.
'''

class Solution0:
    def numIslands(self, grid) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        columns = len(grid[0])
        count = 0

        for i in range(rows):
            for j in range(columns):
                # If we find a "1" (land block), run dfs at that location
                # in the grid.
                if '1' == grid[i][j]:
                    count += 1
                    self.dfs_iterative(grid, i, j)
        return count

    def inRange(self, grid: [[str]], r, c: [str]) -> bool:
        numRow, numCol = len(grid), len(grid[0])
        if r < 0 or c < 0 or r >= numRow or c >= numCol:
            return False
        return True

    def dfs_recursive(self, grid: [[str]], row, col: str) -> None:
        # Mark with a value of -1 if to declare that cell as "seen"
        grid[row][col] = -1

        # directions:  Up,     Down,    Left,    Right
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for d in directions:
            next_row = row + d[0]
            next_col = col + d[1]
            if self.inRange(grid, next_row, next_col) and \
               '1' == grid[next_row][next_col]:
                self.dfs_recursive(grid, next_row, next_col)


'''
Solution Explanation:
    Traverse the grid until we find a land block, then call BFS where we
    enqueues the current cell, marks it as seen, then searches all of its
    neighbors. If the queue is empty, then all lands blocks have been marked
    in the connected island.

If m and n are the number of rows and columns in the grid, respectively, then:
Time Complexity: O(m*n), since we may have to check every value in n for every
    value in m.
Space Complexity: O(min(m,n)), in the worst case where the entire grid is land
    blocks the queue will have at most min(m, n) elements.
'''


class Solution1:
    def inRange(self, grid: [[int]], r, c: [int]) -> bool:
        numRow, numCol = len(grid), len(grid[0])
        if r < 0 or c < 0 or r >= numRow or c >= numCol:
            return False
        return True

    def numIslands(self, grid: [[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        columns = len(grid[0])
        count = 0

        for i in range(rows):
            for j in range(columns):
                # If we find a "1" (land block), run BFS at that location
                # in the grid.
                if "1" == grid[i][j]:
                    self.bfs(grid, i, j)
                    count += 1
        return count

    def bfs(self, grid: [[int]], row, col: int) -> None:
        queue = []
        queue.append((row, col))

        # Mark with a value of -1 if to declare that cell as "seen"
        grid[row][col] = -1

        while queue:
            # directions:  Up,     Down,    Left,    Right
            directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            row, col = queue.pop()

            for d in directions:
                next_row = row + d[0]
                next_col = col + d[1]
                if self.inRange(grid, next_row, next_col) and "1" == grid[next_row][next_col]:
                    queue.append((next_row, next_col))
                    # Mark the cell as seen
                    grid[next_row][next_col] = -1

# Shorter pythonic solution
class Solution2:
    def numIslands(self, grid):
        def sink(i, j):
            # Bounds check
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                # Mark the cell as seen
                grid[i][j] = '#'

                # cast to list since map in python3 returns an iterator
                list(map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1)))
                return 1
            return 0
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))


grid = [["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]]
print(Solution().numIslands(grid))
# 1
