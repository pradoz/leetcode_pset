from typing import List

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = 0
        # left = 0
        # right = 0
        balance = 0 # its like a teeter-totter from the playground

        for ch in s:
            if ch == 'L':
                balance += 1
                # left += 1
            else:
                balance -= 1
                # right += 1
            # if right == left:
            if balance == 0:
                result += 1

        return result








s = ["RLLLLRRRLR","LLLLRRRR","RLRRRLLRLL"]

test_results = [3,1,2]
test_cases = len(test_results)

def run_test() -> None:
    sol = Solution()
    for i in range (test_cases):
        check_test = sol.balancedStringSplit(s[i])
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
