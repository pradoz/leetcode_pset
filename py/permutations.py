from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        # think then code

        n = len(nums)
        if n < 2:
            return [nums]


        for i in range(n):
            others = nums[:i] + nums[i+1:]
            # print(f'calling perms on: {others}')
            other_perms = self.permute(others)
            for p in other_perms:
                # print([nums[i]] + p)
                result.append([nums[i]] + p)
            '''
            for _ in range(n-1):
                perms = [nums[i]]
                for j in range(0, i):
                    perms.append(nums[j])
                for j in range(i+1, n):
                    perms.append(nums[j])
            '''
        return result








nums = [[1,2,3],[0,1],[1]]

test_results = [[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]],
                [[0,1],[1,0]],
                [[1]]
               ]
test_cases = len(test_results)

def run_test() -> None:
    sol = Solution()
    for i in range (test_cases):
        check_test = sol.permute(nums[i])
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
