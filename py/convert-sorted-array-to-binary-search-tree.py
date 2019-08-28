# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Recursive solution, O(n) for time and space since we need to look at every
# node at least once and store every node to construct the tree
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = len(nums) // 2
        low = nums[:mid]
        high = nums[mid+1:]
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(low)
        root.right = self.sortedArrayToBST(high)
        return root

# Helper function to recurse approach
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.bst_helper(nums, 0, len(nums))

    def bst_helper(self, nums, left, right):
        if left >= right:
            return None

        # mid = len(nums) // 2 #
        mid = left + (right - left) // 2
        root = TreeNode(nums[mid])
        root.left = self.bst_helper(nums, left, mid)
        root.right = self.bst_helper(nums, mid+1, right)
        return root

# Ecapsulated helper function
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        def bst_helper(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            
            root.left = bst_helper(left, mid-1)
            root.right = bst_helper(mid+1, right)
            
            return root
        
    
        return bst_helper(0, len(nums) - 1)