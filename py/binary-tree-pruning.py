# We are given the head node root of a binary tree, where additionally every
# node's value is either a 0 or a 1.

# Return the same tree where every subtree (of the given tree) not containing
# a 1 has been removed.

# (Recall that the subtree of a node X is X, plus every node that is a
# descendant of X.)

# Example 1:
# Input: [1,null,0,0,1]
# Output: [1,null,0,null,1]

# Example 2:
# Input: [1,0,1,0,0,0,1]
# Output: [1,null,1,null,1]

# Example 3:
# Input: [1,1,0,1,1,0,1,0]
# Output: [1,1,0,1,1,null,1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


'''
Recursive solution:
Call pruneTree at every subtree.
If the current node is zero, then check if both children are None
'''
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        # Base case one
        if not root:
            return None

        if root.val == 0 and not root.left and not root.right:
            return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if root.val == 0 and not root.left and not root.right:
            return None

        return root


'''
Iterative solution:
We want to visit the subtrees and push their nodes onto the stack
Mark all nodes with root of zero and "None" children with -1
If the node exists and has a value of negative one, set it to None
Return the root
'''
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()
            # Check if the current node is None
            if node:
                # Check if we have visited this node yet
                if not visited:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
                else: # If we haven't visited the node yet
                    if node.left and node.left.val == -1:
                        node.left = None
                    if node.right and node.right.val == -1:
                        node.right = None
                    if not node.left and not node.right and node.val == 0:
                        node.val = -1
        return root