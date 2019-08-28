# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        match_val = root.val

        if root.left:
            if root.left.val != match_val:
                return False
        if root.right:
            if root.right.val != match_val:
                return False

        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)

# using dfs recursively as a helper function
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def dfs(curr: TreeNode) -> None:
            if curr:
                if curr.val != self.match_val:
                    self.is_unival_bst = False
                else:
                    dfs(curr.left)
                    dfs(curr.right)

        if not root:
            return True

        self.match_val = root.val
        self.is_unival_bst = True
        dfs(root)
        return self.is_unival_bst


# using iterative dfs
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        check = root.val
        stack = []
        while True:
            if root:
                stack.append(root)
                root = root.left
            else:
                if not stack:
                    break
                root = stack.pop()
                if root.val != check:
                    return False
                root = root.right
        return True

# using a deque from collections
from collections import deque

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        match_val = root.val
        q = deque([root])

        while len(q):
            node = q.popleft()

            if not node:
                continue
            if node.val != match_val:
                return False

            q.append(node.left)
            q.append(node.right)

        return True




