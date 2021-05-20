from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# BFS
# O(n) time
# O(n) space
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        queue = deque([(root, 0)])

        while queue:
            node, level = queue.popleft()
            if node:
                if level + 1 > len(result):
                    result.append([])
                result[level].append(node.val)
                children = (node.left, node.right)
                for child in children:
                    queue.append((child, level + 1))
        return result


# DFS
# O(n^2) time
# O(n) space
class Solution0:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def helper(node: TreeNode, result: List[List[int]], level: int) -> None:
            if not node:
                return

            if level + 1 > len(result):
                result.append([])

            result[level].append(node.val)
            children = (node.left, node.right)
            for child in children:
                helper(child, result, level + 1)

        result = []
        helper(root, result, 0)
        return result








nums = []

test_results = []
test_cases = len(test_results)

def run_test() -> None:
    sol = Solution()
    for i in range (test_cases):
        check_test = sol.func()
        test_flag = True if check_test == test_results[i] else False
        if test_flag == True:
            print(f'++++ TEST #{i+1}: SUCCESS. Result = {check_test}')
        else:
            print(f'---- TEST #{i+1}: FAILURE.')
            print(f'       Expected: {test_results[i]}')
            print(f'       Received: {check_test}')

def main() -> None:
    run_test()

if __name__ == '__main__':
    main()
