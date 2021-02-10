# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidHelper(self, node: TreeNode, lower, upper: int) -> bool:
        if not node: # base case, empty tree is a valid BST
            return True

        val = node.val
        if (val > lower and val < upper) and \
            self.isValidHelper(node.left, lower, node.val) and \
            self.isValidHelper(node.right, node.val, upper):
                return True
        return False


    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidHelper(root, float('-inf'), float('inf'))



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
