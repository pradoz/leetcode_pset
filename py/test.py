class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        target -= 30
        seen = {}
        if len(nums) == 2:
            return [0, 1]

        ret = [0, 0]
        tmp = [0, 0]
        for i, v in enumerate(nums):
            comp = target - v
            if comp in seen:
                tmp = [i, seen[comp]] if nums[i] < nums[seen[comp]] else [seen[comp], i]
                if ret:
                    ret = ret if nums[ret[1]] > nums[ret[1]] else tmp
                else:
                    ret = tmp
                    ret = [seen[comp], i]
            else:
                dist = comp - nums[i]
                seen[dist] = i

            seen[v] = i
        return ret

target = 90
nums = [50, 20, 10, 40]
print(Solution().twoSum(nums, target))
# [0, 2]
nums = [20, 50, 40, 25, 30, 10]
print(Solution().twoSum(nums, target))
# [5, 1]