# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        total = [0]
        self.dfs(root, L, R, total)
        return total[0]

    '''
    Downside to dfs, recursion limits memory to stack space
    This is okay here, based on limits given 
      1) The number of nodes in the tree is at most 10000.
      2) The final answer is guaranteed to be less than 2^31.
    '''
    def dfs(self, root, L, R, total) -> None:
        """ depth first search the binary tree """
        if not root:
            return
        if L <= root.val <= R:
            total[0] += root.val
        if root.val > L:
            self.dfs(root.left, L, R, total)
        if root.val < R:
            self.dfs(root.right, L, R, total)

    # # Solution without dfs
    # def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    #     if not root:
    #         return 0

    #     total = 0

    #     if L <= root.val <= R:
    #         total += root.val
    #         total += self.rangeSumBST(root.left, L, R)
    #         total += self.rangeSumBST(root.right, L, R)
    #     elif root.val < L:
    #         total += self.rangeSumBST(root.right, L, R)
    #     elif root.val > R:
    #         total += self.rangeSumBST(root.left, L, R)
    #     return total