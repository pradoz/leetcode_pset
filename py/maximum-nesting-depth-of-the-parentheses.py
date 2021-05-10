from typing import List

class Solution:
    def maxDepth(self, s: str) -> int:
        result = 0
        # go through and see the biggest left parenthesis
        # shouldn't have to worry about balancing, just the max depth
        depth = 0
        for ch in s:
            if ch == '(':
                depth += 1
                result = max(result, depth)
            elif ch == ')':
                depth -= 1

            # only need to check if we increase depth
            # result = max(result, depth)

        return result








s = ["(1+(2*3)+((8)/4))+1","(1)+((2))+(((3)))","1+(2*3)/(2-1)","1"]

test_results = [3,3,1,0]
test_cases = len(test_results)

def run_test() -> None:
    sol = Solution()
    for i in range (test_cases):
        check_test = sol.maxDepth(s[i])
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
