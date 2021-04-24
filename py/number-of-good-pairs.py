from typing import List
from collections import defaultdict

# O(n) runtime, O(1) space
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        seen = {}

        for i, num in enumerate(nums):
            if num not in seen:
                seen[num] = 1
            else:
                result += seen[num]
                seen[num] += 1

        return result


# O(n*k) runtime, k is the number of repeats
# O(k) space
class Solution1:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        pairs = []

        # for each number in nums, store the index it was seen at
        # if we find something we've seen, then that is the upper bound, and
        # seen[nums[i]] ==> lower bound
        seen = defaultdict(list)

        '''
        seen = {
                1: [0, 3, 4]
                2: [1]
                3: [2]
            }
        [1,2,3,1,1,3],
        '''

        for i, num in enumerate(nums):
            if num not in seen:
                seen[num] = [i]
            else:
                for _ in range(len(seen[num])):
                    pairs.append((seen[num], i))
                seen[num].append(i)

        result = len(pairs)
        return result


# O(n^2) runtime solution
# O(1) memory
class Solution0:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        pairs = []
    
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j] and i < j:
                    pairs.append((i, j))

        result = len(pairs)
        return result








nums = [
        [1,2,3,1,1,3],
        [1,1,1,1],
        [1,2,3],
       ]

test_results = [4, 6, 0]
test_cases = len(test_results)

def run_test() -> None:
    sol = Solution()
    for i in range (test_cases):
        check_test = sol.numIdenticalPairs(nums[i])
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
