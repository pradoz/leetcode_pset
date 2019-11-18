'''
Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
# O(n^2) runtime solution, O(1) extra space
class Solution0:
    def twoSum(self, nums: [int], target: int) -> [int]:
        if len(nums) == 2:
            return [0, 1]

        for i in range(len(nums)):
            for j in range(i + j + 1, len(nums)):
                check = nums[i] + nums[j]
                if target == check:
                    return [i, j]

# O(n) runtime+space solution, where n is the # of unique integers in nums
class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        distances = {}

        # preprocess, then check
        for i, num in enumerate(nums):
            if (target - num) in distances:
                return [i, distances[target - num]]
            distances[num] = i





nums = [3,4,7]
target = 11
print(Solution().twoSum(nums, target))
nums = [2,7,11,15]
target = 9
# print(Solution().twoSum(nums, target))