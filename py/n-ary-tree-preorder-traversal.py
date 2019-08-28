"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
# basic recursive solution
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = [root.val]
        for child in root.children:
            result.extend(self.preorder(child))
        return result

# inefficient space solution since we store every node, but much faster
# than most approaches to this problem
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        nodes = [root]
        out = []

        while nodes:
            temp = nodes.pop()
            out.append(temp.val)

            for child in reversed(temp.children):
                nodes.append(child)
        return out

# interesting assignment to 'nodes' makes this code look much cleaner/pythonic
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ret = []
        nodes = root and [root]
        while nodes:
            node = nodes.pop()
            ret.append(node.val)
            nodes += [child for child in reversed(node.children) if child]
        return ret

# Using a stack
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        stack = [root]
        ret = []
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                stack += [child for child in reversed(node.children) if child]
        return ret

# Helper function (DFS-ish)
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ret = []
        self.helper(root, ret)
        return ret
    def helper(self, root, ret: 'Node') -> None:
        if not root:
            return
        ret.append(root.val)
        if root.children:
            for kid in root.children:
                self.helper(kid, ret)
            # map(self.helper, root.children, ret) # didn't work
        return

# DFS, only pass the node by defining the function inside preorder
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def dfs(node: 'Node') -> None:
            if not node:
                return
            ans.append(node.val)
            for c in node.children:
                dfs(c)
        ans = []
        dfs(root)
        return ans










