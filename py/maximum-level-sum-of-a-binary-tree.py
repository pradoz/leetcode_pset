# Given the root of a binary tree, the level of its root is 1, the level of
# its children is 2, and so on.

# Return the smallest level X such that the sum of all the values of nodes at
# level X is maximal.

# DFS
# Time and space are both O(n), where n is the number of nodes. We have to
# visit each node, and store every node in the worst case.
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, lst: [TreeNode], level: int) -> None:
            if not root:
                return
            if len(lst) == level:
                lst.append(root.val)
            else:
                lst[level] += root.val
            dfs(root.left, lst, level + 1)
            dfs(root.right, lst, level + 1)

        lst = []
        dfs(root, lst, 0)
        print(lst)
        return lst.index(max(lst)) + 1


# Using BFS and a deque from collections
from collections import deque
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        max_sum = float('-inf')
        curr_level = 0
        max_level = 0

        q = deque()
        q.append(root)
        while q:
            curr_level += 1
            curr_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                curr_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if max_sum < curr_sum:
                max_sum = curr_sum
                max_level = curr_level
        return max_level


# Calculate sums at each level, then append all children on the next level to a
# list, then repeat until that list is empty. Keep track of the max sum/index.
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        level = [root]
        max_sum = float('-inf')
        max_level = -1
        curr_level = 1
        while level:
            curr_sum = 0

            for node in level:
                curr_sum += node.val
            # max_sum = max(max_sum, curr_sum)
            # max_level = max(max_level, curr_level)
            if curr_sum > max_sum:
                max_sum = curr_sum
                max_level = curr_level
            level = [child for node in level for child in (node.left, node.right) if child is not None]
            curr_level += 1
        return max_level




