"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

# Recursively
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        if root.children is None:
            return [root.val]

        result = []
        res = []
        for child in root.children:
            res += self.postorder(child)
        result += res
        result.append(root.val)
        return result

# Iteratively
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        stack = [root]
        res = []
        while stack and root:
            n = stack.pop()
            res.insert(0, n.val)
            stack += n.children
        return res

# Recursively with post_order_traversal function
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def post_order_traversal(node: 'Node') -> None:
            if not node:
                return
            for child in node.children:
                post_order_traversal(child)
            res.append(node.val)
        post_order_traversal(root)
        return res


# Iteratively with helper function to minimize work
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        def traverse_and_check(x: 'Node'):
            # lets us reference it outside the scope without
             # passing it as a parameter
            nonlocal res
            if x:
                # if x has no children, just append x's val
                if not x.children:
                    res.append(x.val)
                else: # else append every child for every child
                    for child in x.children:
                        traverse_and_check(child)
                    res.append(x.val)
        # End of traverse_and_check()
        if root:
            traverse_and_check(root)
        return res









