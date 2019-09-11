'''
Return the root node of a binary search tree that matches the given
preorder traversal.

Example 1:
Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Solution Explanation:
1. Keep a counter and constuct nodes until we reach the size of the list.
2. Create a new, root and increment the counter.
3. Recursively call bstFromPreorder() on the current node's left subtree and
    right subtree.
'''

# Using Bounds Algorithm:
# Time complexity: O(n) since we call bstFromPreorder exactly n times.
# Space complexity: O(n), in the worst case we have to store all of the nodes
#   as we construct the tree
class Solution:
    def __init__(self):
        self.i = 0

    def bstFromPreorder(self, preorder: List[int], upper_bound = float('inf')) -> TreeNode:
        if self.i == len(preorder) or preorder[self.i] > upper_bound:
            return None

        root = TreeNode(preorder[self.i])
        self.i += 1

        # Recursive call to left subtree
        root.left = self.bstFromPreorder(preorder, root.val)
        # Recursive call to right subtree
        root.right = self.bstFromPreorder(preorder, upper_bound)
        return root


''' Explanation (iteratively using a stack)
Constant space on average, still have degenerate trees with case of O(n)
preorder[0] becomes the root.
For next item in preorder list, there are 2 cases to consider:
    If value is less than last item in stack, it is the left child of last item
    If value is greater than last item in stack, pop it
The last popped item will be the parent and the item will be the right child
of the parent.
'''
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        stack = [root]
        for value in preorder[1:]:
            if value < stack[-1].val:
                stack[-1].left = TreeNode(value)
                stack.append(stack[-1].left)
            else:
                while stack and stack[-1].val < value:
                    last = stack.pop()
                last.right = TreeNode(value)
                stack.append(last.right)
        return root

'''
Solution Explanation:
1. If the list is empty, we cannot construct a tree.
2. If the list has elements, then the root is the first node in the list.
3. Bisect the list where values stop decreasing/start increasing.
4. Recursively call bstFromPreorder() on the left subtree, defined by
    indexes [1,i), and on the right subtree from [i,len([preorder])).
'''

# Slightly better Algorithm:
# Time complexity: O(n*logn) since we use a helper function to break up the
#   work we have to do at each level, giving logarithmic runtime.
# Space complexity: O(n), in the worst case we have to store all of the nodes
#   as we construct the tree.
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def help_construct_from_preorder(i, j: int) -> TreeNode:
            if i == j: return None
            root = TreeNode(preorder[i])
            mid = bisect.bisect(preorder, preorder[i], i+1, j)
            root.left = help_construct_from_preorder(i+1, mid)
            root.right = help_construct_from_preorder(mid, j)
            return root

        # if not preorder:
        #     return None
        return help_construct_from_preorder(0, len(preorder))


'''
Solution Explanation:
1. If the list is empty, we cannot construct a tree.
2. If the list has elements, then the root is the first node in the list.
3. Traverse the elements in the list until we find a value greater than root.
4. Recursively call bstFromPreorder() on the left subtree, defined by
    indexes [1,i), and on the right subtree from [i,len([preorder])).
'''

# Naive Algorithm:
# Time complexity: O(n^2) in the worst case since we have to check every
#   subtree for every subtree, and n is the number of nodes who have subtrees
#   to check. O(nlogn) on average due to splitting of work and n traversals to
#   reach the bottom of the tree.
# Space complexity: O(n), in the worst case we have to store all of the nodes
#   as we construct the tree.
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val) # Creates root with value 8

        i = 1
        while i < len(preorder):
            # Traverse until we find a break condition (an increasing value)
            if preorder[i] > root_val:
                break;
            i += 1
        # Recursive call to left subtree
        root.left = self.bstFromPreorder(preorder[1:i])
        # Recursive call to right subtree
        root.right = self.bstFromPreorder(preorder[i:])
        return root


preorder = [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]
Solution().bstFromPreorder(preorder)