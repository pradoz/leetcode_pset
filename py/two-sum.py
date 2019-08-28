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
class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        if len(nums) == 2:
            return [0, 1]

        lst = []
        for i in range(len(nums)):
            lst.append(nums[i])
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]


class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        # target -= 30
        seen = {}
        if len(nums) == 2:
            return [0, 1]

        ret = [None, None]
        for i, v in enumerate(nums):
            comp = target - v
            if comp in seen:
                return [seen[comp], i]
            seen[v] = i





nums = [3,4,2]
target = 6
print(Solution().twoSum(nums, target))
nums = [2,7,11,15]
target = 9
# print(Solution().twoSum(nums, target))