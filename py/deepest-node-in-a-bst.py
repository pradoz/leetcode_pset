# Hi, here's your problem today. This problem was recently asked by Google:

# You are given the root of a binary tree.
# Return the deepest node (the furthest node from the root).

# Example:
#     a
#    / \
#   b   c
#  /
# d
# The deepest node in this tree is d at depth 3.

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        # string representation
        return self.val


# Time: O(n)
# Space: O(log n) average, O(n) in the case of a degenerate tree (one branch)
def deepest(node: Node):
    if node and not node.left and not node.right:
        return (node, 1) # the root is the only node, depth = 1

    # if the deepest node is in the right subtree
    # elif the deepest node is in the left subtree
    if not node.left:
        return increment_depth(deepest(node.right))
    elif not node.right:
        return increment_depth(deepest(node.left))

    # increment depth using the tuple with higher depth
    return increment_depth(
                max(deepest(node.left),
                    deepest(node.right), key=lambda x: x[1]))[0]


def increment_depth(node_depth_tup):
    node, depth = node_depth_tup
    return (node, depth + 1)



root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')

print(deepest(root))
# (d, 3)

############### LeetCode Version ###############

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        # string representation
        return self.val

# Using Depth-first search
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> (int, TreeNode):
        def dfs(node: TreeNode):
            if not node:
                return (0, None)

            lhs, rhs = dfs(node.left), dfs(node.right)
            if lhs[0] > rhs[0]:
                return (lhs[0] + 1, lhs[1])
            
            if lhs[0] < rhs[0]:
                return (rhs[0] + 1, rhs[1])
            else:
                return (lhs[0] + 1, node)
            ## end of dfs()
        return dfs(root)[1]


# using tuples
class Solution:
    def returnDepth(self, root: TreeNode) -> (int, TreeNode):
        if not root:
            return (0, None)

        (left_depth, left_node) = self.returnDepth(root.left)
        (right_depth, right_node) = self.returnDepth(root.right)

        if left_depth == right_depth:
            return (left_depth + 1, root)
        elif right_depth > left_depth:
            return (right_depth + 1, right_node)
        else:
            return (left_depth + 1, left_node)
    
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        depth, node = self.returnDepth(root)
        return node
        



print(Solution().subtreeWithAllDeepest(root))



