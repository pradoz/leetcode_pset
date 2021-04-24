from typing import List

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        result = 0
        prev = 0
        curr = 1

        for i in range(1, len(s)):
            print(prev, curr, result)
            if s[i-1] != s[i]:
                result += min(curr, prev)
                prev = curr
                curr = 1
            else:
                curr += 1
        result += min(curr, prev)

        return result








st = ["00110011", "10101"]

test_results = [6, 4]
test_cases = len(test_results)

def run_test() -> None:
    s = Solution()
    for i in range (test_cases):
        check_test = s.countBinarySubstrings(st[i])
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
