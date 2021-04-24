from typing import List

# O(n) time+space
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        result = [''] * n

        for i, new_ind in enumerate(indices):
            result[new_ind] = s[i]

        return ''.join(result)








s = ["codeleet", "abc", "aiohn"]
indices = [
            [4,5,6,7,0,2,1,3],
            [0,1,2],
            [3,1,4,2,0],
          ]

test_results = ["leetcode", "abc", "nihao"]
test_cases = len(test_results)

def run_test() -> None:
    sol = Solution()
    for i in range (test_cases):
        check_test = sol.restoreString(s[i], indices[i])
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
