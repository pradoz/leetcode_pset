from typing import List

class Solution:
    def func(self) -> int:
        result = 0
        # think then code

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
