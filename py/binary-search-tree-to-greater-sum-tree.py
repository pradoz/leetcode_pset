'''
Given the root of a binary search tree with distinct values, modify it so that
every node has a new value equal to the sum of the values of the original tree
that are greater than or equal to node.val.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

Note:
The number of nodes in the tree is between 1 and 100.
Each node will have value between 0 and 100.
The given tree is a binary search tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive solution with helper function to handle recursive calls
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.recursive_helper(root, 0)
        return root

    def recursive_helper(self, root: TreeNode, prev: int) -> int:
        if root is None: return prev 

        res = self.recursive_helper(root.right, prev)
        root.val += res

        return self.recursive_helper(root.left, root.val)


# Recursive solution with encapsulated helper function
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def recursive_helper(root: TreeNode, prev: int) -> int:
            if root is None: return prev 

            res = recursive_helper(root.right, prev)
            root.val += res

            return recursive_helper(root.left, root.val)
        recursive_helper(root, 0)
        return root



# Using a stack
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root is None: return root

        prev = 0
        stack = []
        curr = root

        while curr or len(stack) > 0:
            while curr:
                stack.append(curr)
                curr = curr.right
            curr = stack.pop()
            curr.val += prev
            prev = curr.val
            curr = curr.left
        return root


# Using a deque
from collections import deque

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root is None: return root

        prev = 0
        q = deque()
        curr = root

        while curr or len(q) > 0:
            while curr:
                q.append(curr)
                curr = curr.right
            curr = q.pop()
            curr.val += prev
            prev = curr.val
            curr = curr.left
        return root





        