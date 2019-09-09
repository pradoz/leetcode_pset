'''
Given the root node of a binary search tree (BST) and a value to be inserted
into the tree, insert the value into the BST. Return the root node of the
BST after the insertion. It is guaranteed that the new value does not exist
in the original BST.

Note that there may exist multiple valid ways for the insertion, as long
as the tree remains a BST after insertion. You can return any of them.

(See Leetcode site for example tree diagrams)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Time Complexity: O(nlogn) on average, but O(n) in the worst case of a
#                  degenerate tree (similar to a linked list)
# Space Complexity: O(n) since in the worst case we store the entire recursion
#                   stack at every node.

# Basic recursive solution
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # If no root exists, create one
        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else: # elif val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        return root


# A slightly better recursive solution
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        if val < root.val:
            if not root.left:
                node = TreeNode(val)
                root.left = node
            else:
                self.insertIntoBST(root.left, val)
        else:
            if not root.right:
                node = TreeNode(val)
                root.right = node
            else:
                self.insertIntoBST(root.right, val)
        return root


# Iterative solution (uses O(1) extra space)
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        curr = root
        while curr:
            if val < curr.val:
                if not curr.left:
                    curr.left = TreeNode(val)
                    break
                else:
                    curr = curr.left
            else:
                if not curr.right:
                    curr.right = TreeNode(val)
                    break
                else:
                    curr = curr.right
        return root