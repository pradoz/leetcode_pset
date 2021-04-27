from typing import List

# O(log_10(n)) time + space
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        result = 0
        prod = 1
        nums_sum = 0

        while n > 0:
            digit = n % 10
            n //= 10
            prod *= digit
            nums_sum += digit
        result = prod - nums_sum
        return result



class Solution0:
    def subtractProductAndSum(self, n: int) -> int:
        result = 0
        nums = []

        while n > 0:
            digit = n % 10
            n //= 10
            nums.append(digit)
        
        prod = 1
        nums_sum = 0
        for num in nums:
            prod *= num
            nums_sum += num

        result = prod - nums_sum
        return result








n = [234, 4421]

test_results = [15, 21]
test_cases = len(test_results)

def run_test() -> None:
    sol = Solution()
    for i in range (test_cases):
        check_test = sol.subtractProductAndSum(n[i])
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
