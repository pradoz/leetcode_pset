from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        mid = 0

        while left < right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else: # target < nums[mid]
                right = mid
        # return mid
        return left







nums = [
        [1,3,5,6],
        [1,3,5,6],
        [1,3,5,6],
        [1,3,5,6],
        [1],
        [1,3],
        [1,3],
        [1],
       ]
target = [5, 2, 7, 0, 0, 2, 3, 1]

test_results = [2, 1, 4, 0, 0, 1, 1, 0]
test_cases = len(test_results)

def run_test() -> None:
    s = Solution()
    for i in range (test_cases):
        check_test = s.searchInsert(nums[i], target[i])
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
