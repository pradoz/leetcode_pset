class Solution(object):
    def inRange(self, grid, r, c):
        numRow, numCol = len(grid), len(grid[0])
        if r < 0 or c < 0 or r >= numRow or c >= numCol:
            return False
        return True

    # Counts the number of islands using
    # a breadth first search.
    def numIslandsBFS(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        rows, columns = len(grid), len(grid[0])
        count = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j)
                    count += 1
        return count

    # Runs breadth first search on the current
    # row and column.
    def bfs(self, grid, currRow, currCol):
        queue = []
        queue.append((currRow, currCol))
        # mark current vertex as visited
        grid[currRow][currCol] = 2
    
        while queue:
            directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            currRow, currCol = queue.pop()
            for d in directions:
                nextRow, nextCol = currRow + d[0], currCol + d[1]
                if self.inRange(grid, nextRow, nextCol) and grid[nextRow][nextCol] == 1:
                    queue.append((nextRow, nextCol))
                    # mark next vertex and column as visited so
                    # we don't double count
                    grid[nextRow][nextCol] = 2


grid = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0]]
print(Solution().numIslandsBFS(grid))
# 3
grid = [[1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]]
print(Solution().numIslandsBFS(grid))
# 1