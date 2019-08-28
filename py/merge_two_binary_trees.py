# merge_two_binary_trees.py

'''
Given two binary trees and imagine that when you put one of them to cover the
other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two
nodes overlap, then sum node values up as the new value of the merged node.
Otherwise,the NOT null node will be used as the node of new tree.
'''

# Example:
# Input: 
#     Tree 1                     Tree 2
#           1                         2
#          / \                       / 
#         3   2                     1   
#        /                           \   
#       5                             4   
# Output:
#          3
#         / \
#        4   5
#       / \   \ 
#      5   4   7
# Note: The merging process must start from the root nodes of both trees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

## Strategy:
# If one tree doesn't exist, we return the other tree and do nothing else.
# If they overlap, we need to add the nodes values
# If they don't overlap, we need to connect them.
# We can use impose t2 on t1, so all values get updated in t1

# Time: O(n), where n is the number of nodes in the tree
# Space: O(h), where h is log_2(n)

# Recursive solution
class Solution():
    def mergeTrees(self, t1, t2: TreeNode) -> TreeNode:
        def merge(t1, t2: TreeNode) -> TreeNode:
            if not t2:
                return t1
            if not t1:
                return t2

            t1.val += t2.val

            t1.left = merge(t1.left, t2.left)
            t1.right = merge(t1.right, t2.right)
            return t1

        t1 = merge(t1, t2)
        return t1

# Iterative solution
# Trade-offs:
# Lower space complexity, longer run time, harder to do in-place
class Solution1():
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t2:
            return t1
        if not t1:
            return t2
        
        stack = [(t1, t2)]

        while stack:
            n1, n2 = stack.pop()

            if n1 and n2:
                n1.val += n2.val

            if not n1.right:
                n1.right = n2.right
            elif n2.right:
                stack.append((n1.right, n2.right))

            if not n1.left:
                n1.left = n2.left
            elif n2.left:
                stack.append((n1.left, n2.left))

        return t1





