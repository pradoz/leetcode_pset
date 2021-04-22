from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0

        for customer in accounts:
            max_wealth = max(max_wealth, sum(customer))
        return max_wealth



accounts = [
            [[1,2,3],[3,2,1]],
            [[1,5],[7,3],[3,5]],
            [[2,8,7],[7,1,3],[1,9,5]],
           ]

test_results = [6, 10, 17]
test_cases = len(test_results)

def run_test() -> None:
    s = Solution()
    for i in range (test_cases):
        check_test = s.maximumWealth(accounts[i])
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
