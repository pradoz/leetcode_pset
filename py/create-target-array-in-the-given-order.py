from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n

        for i in range(n):
            self.insert(nums[i], index[i], i, result)

        return result

    def insert(self, num: int, i: int, j: int, result: List[int]) -> None:
        if result[i] == -1:
            result[i] = num
            return
        
        # else
        while i <= j:
            temp = result[i]
            result[i] = num
            num = temp
            i += 1










nums = [[0,1,2,3,4],[1,2,3,4,0],[1]]
index = [[0,1,2,2,1], [0,1,2,3,0], [0]]

test_results = [[0,4,1,3,2], [0,1,2,3,4], [1]]
test_cases = len(test_results)

def run_test() -> None:
    sol = Solution()
    for i in range (test_cases):
        check_test = sol.createTargetArray(nums[i], index[i])
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
