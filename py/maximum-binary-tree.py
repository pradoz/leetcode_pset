'''
Given an integer array with no duplicates. A maximum tree building on this
array is defined as follow:

  1. The root is the maximum number in the array.
  2. The left subtree is the maximum tree constructed from left part subarray 
    divided by the maximum number.
  3. The right subtree is the maximum tree constructed from right part subarray 
    divided by the maximum number.

Construct the maximum tree by the given array and output the root node of
this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
   \\    / 
     2  0   
       \
        1
'''
# Both solution complexity analysis:
# Time: O(n)
# Space: O(n)

# Explanation: we need to look at every node to find the max, and store every
#     we need to node and we need to store every node to construct the tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Recursive solution
class Solution0:
    def constructMaximumBinaryTree(self, nums: [int]) -> TreeNode:
        # early exit case
        if not nums:
            return 

        # check base case
        if len(nums) == 1:
            return TreeNode(nums[0])

        # find the max value
        max_val = max(nums)

        # max_val = 0
        # for num in nums:
        #     max_val = max(max_val, num)

        root = TreeNode(max_val)
        index_of_max_val = nums.index(max_val)
        root.left = self.constructMaximumBinaryTree(nums[0:index_of_max_val])
        root.right = self.constructMaximumBinaryTree(nums[index_of_max_val+1:])
        return root


# Iterative solution with a stack
class Solution:
    def constructMaximumBinaryTree(self, nums: [int]) -> TreeNode:
        # early exit case
        if not nums:
            return 

        # check base case
        if len(nums) == 1:
            return TreeNode(nums[0])

        stack = []

        # append every node to the stack with num as its initialized value
        for num in nums:
            node = TreeNode(num)

            # while the stack isn't empty
            while stack and num > stack[-1].val:
                node.left = stack.pop()
            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]




Solution().constructMaximumBinaryTree([3,2,1,6,0,5])