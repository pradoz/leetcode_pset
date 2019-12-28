# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict

class Solution:
    def __repr__(self):
        if self.left and self.right:
            return f'{self.val}, {self.left}, {self.right}'
        if self.left:
            return f'{self.val}, {self.left}'
        if self.right:
            return f'{self.val}, {self.right}'
        return f'{self.val}'


    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        # map containing all subtrees as keys and duplicate counts as values
        subtreeCount = defaultdict(lambda: 0)
        duplicateSubtrees = []

        # DFS
        def serializeSubtrees(root: TreeNode):
            if root is None:
                return ''

            # these call __repr__
            left = serializeSubtrees(root.left)
            right = serializeSubtrees(root.right)

            # construct result string
            result = f'{root.val} {left} {right}'

            # add the subtree to the map
            subtreeCount[result] += 1

            # check for duplicates
            if subtreeCount[result] == 2:
                duplicateSubtrees.append(root)

            return result

        serializeSubtrees(root)
        return duplicateSubtrees