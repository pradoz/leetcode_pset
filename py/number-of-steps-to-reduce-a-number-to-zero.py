from typing import List

class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0

        result = 0
        
        # if the bit is 0, we add 1 because we would divide by two
        # if the bit is 1, we add 2 b/c we minus one then divide by two
        while num > 0:
            result += 1 + (num & 1)
            num = num >> 1

        return result - 1


class Solution0:
    def numberOfSteps(self, num: int) -> int:
        # Given a non-negative integer num, return the number of steps to
        # reduce it to zero.

        # If the current number is even, you have to divide it by 2,
        # otherwise, you have to subtract 1 from it.
        result = 0
        
        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            result += 1

        return result







num = [14, 8, 123]

test_results = [6, 4, 12]
test_cases = len(test_results)

def run_test() -> None:
    sol = Solution()
    for i in range (test_cases):
        check_test = sol.numberOfSteps(num[i])
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
