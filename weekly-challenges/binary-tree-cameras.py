# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# state 2 = covered
# state 1 = covering
# state 0 = to be covered
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return 2

            l = dfs(node.left)
            r = dfs(node.right)

            # we found the parent of a leaf
            # --> needs a camera
            if l == 0 or r == 0:
                self.count += 1
                return 1

            # the current node is covered by a camera
            if l == 1 or r == 1:
                return 2
            # else:
            return 0 # we are at a leaf

        self.count = 0

        flag = dfs(root) == 0 # case where the tree is one node
        return flag + self.count








nums = []

test_results = []
test_cases = len(test_results)

def run_test() -> None:
    sol = Solution()
    for i in range (test_cases):
        check_test = sol.minCameraCover(None)
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
