# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node: TreeNode, lower, upper: int) -> bool:
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False

            if not (helper(node.right, val, upper) or (node.left, lower, val)):
                return False
            if not helper(node.left, lower, val):
                return False
            return True
        return helper(root, float('-inf'), float('inf'))

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        prev = None
        curr = root
        stack = []
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            s = stack.pop()
            if prev and s <= prev.val:
                return False
            prev = s
            curr = s.right
        return True