from typing import List

# O(n log n) time, due to sorting and n iterations
# O(n) space
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        map_to_indexes = {}
        for i, num in enumerate(sorted(nums)):
            if num not in map_to_indexes: # record the earlest index
                map_to_indexes[num] = i

        # the first index it was seen in the sorted list is equal to the amount
        # of numbers smaller than itself
        return [map_to_indexes[num] for num in nums]

# O(n^2) naive implementation
# O(1) space
class Solution0:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if nums[j] < nums[i]:
                    result[i] += 1

        return result








nums = [
        [8,1,2,2,3],
        [6,5,4,8],
        [7,7,7,7],
       ]

test_results = [
                [4,0,1,1,3],
                [2,1,0,3],
                [0,0,0,0],
               ] 

test_cases = len(test_results)

def run_test() -> None:
    sol = Solution()
    for i in range (test_cases):
        check_test = sol.smallerNumbersThanCurrent(nums[i])
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
