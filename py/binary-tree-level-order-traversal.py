# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Traverser helper function
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.levels = []
        self.traversal(root, 0)
        return self.levels

    def traversal(self, node, level) -> None:
        if node:
            if len(self.levels) <= level:
                self.levels += [[node.val]]
            else:
                self.levels[level] += [node.val]
            self.traversal(node.left, level + 1)
            self.traversal(node.right, level + 1)

# DFS recursively
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.dfs(root, 0, res)
        return res
    def dfs(self, root, level, res):
        if not root:
            return
        if len(res) < level + 1:
            res.append([])
        res[level].append(root.val)
        self.dfs(root.left, level + 1, res)
        self.dfs(root.right, level + 1, res)

        
# DFS iteratively using a stack by checking for null pointers to left/right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        stack = [(root, 0)]

        while stack:
            curr_node, level = stack.pop()
            if len(res) < level + 1:
                res.append([])

            res[level].append(curr_node.val)

            # Right before left to maintain order with a stack
            if curr_node.right:
                stack.append((curr_node.right, level + 1))
            if curr_node.left:
                stack.append((curr_node.left, level + 1))
        return res


# DFS iteratively using a stack by just checking if the node is null
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        stack = [(root, 0)]

        while stack:
            curr_node, level = stack.pop()
            if curr_node:
                if len(res) < level + 1:
                    res.append([])

                res[level].append(curr_node.val)
                stack.append((curr_node.right, level + 1))
                stack.append((curr_node.left, level + 1))
        return res


# BFS with a queue
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        queue = [(root, 0)]

        while queue:
            # we are popping at the 0th index (FIFO)
            curr, level = queue.pop(0)
            if curr:
                if len(res) < level + 1:
                    res.append([])    
                res[level].append(curr.val)

                # Left before right with a queue to maintain order
                queue.append((curr.left, level+1))
                queue.append((curr.right, level+1))
        return res

# BFS with a deque from collections
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        deq = deque([(root, 0)])

        while deq:
            curr, level = deq.popleft()
            if curr:
                if len(res) < level + 1:
                    res.append([])    
                res[level].append(curr.val)

                # Left before right while deque'ing to maintain order
                deq.append((curr.left, level+1))
                deq.append((curr.right, level+1))
        return res


