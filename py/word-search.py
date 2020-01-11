class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        self.word = word
        self.found = False

        for row in range(len(board)):
            for col in range(len(board[0])):
                self.visited = [] # stack of visited coordinates
                self.visitedSet = set() # tracks coordinates of the current set of visited characters
                self.dfs(board, row, col, 0)
                if self.found == True:
                    return True
        return False

    def dfs(self, board: [[str]], row, col, idx: int) -> None:
        if idx == len(self.word):
            self.found = True
            return # exit early
        if not self.found \
           and self.withinBounds(row, col, len(board), len(board[0])) \
           and self.isValidNext(board[row][col], self.word[idx], (row, col), self.visitedSet):

            # get visited coordinates
            self.visited += [(row, col)]
            self.visitedSet.add((row, col))

            RIGHT = row + 1
            LEFT = row - 1
            UP = col + 1
            DOWN = col - 1

            # call dfs in adjacent directions and increase the index
            self.dfs(board, RIGHT, col, idx + 1) # Right
            self.dfs(board, LEFT, col, idx + 1) # Left
            self.dfs(board, row, UP, idx + 1) # Up
            self.dfs(board, row, DOWN, idx + 1) # Down

            if not self.found:
                self.visitedSet.remove(self.visited.pop())

    def withinBounds(self, row, col, rowLength, colLength: int) -> bool:
        """ returns true if we can check everywhere around the current location
        in the wordsearch. """
        return row >= 0 and col >= 0 and row < rowLength and col < colLength

    def isValidNext(self, currCell, currLetter: str, \
                          coords: (int, int), currVisitedSet: set((int, int))) -> bool:
        """ returns true if the cell we are searching matches the next letter
        in the word we are looking for. """
        return currCell == currLetter and coords not in currVisitedSet



board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

print(Solution().exist(board, "ABCCED")) # true
print(Solution().exist(board, "SEE")) # true
print(Solution().exist(board, "ABCB")) # false