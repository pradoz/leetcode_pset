'''
Brute force solution:
  1. Generate all possible subsequences.
  2. Check all subsequences to see if they are increasing.
  3. Keep track of the length of the longest subsequence.

This algorithm runs in polynomial time complexity O(2^n) because at each
position n, you have two choices, either include it or not. This gives us:
2 * 2 * 2 * 2 * 2 ... = 2^n, where we are multiplying n 2's together.

Recursive approach:
  1. Empty list returns 0.
  2. One element lists return 1.
  3. For every element to the current element's left that the current element
     is greater than, the longest increasing subsequence ending at the current
     element is "1 + (the longest increasing subsequence ending at an index to
     its left)."
    --> We simply need to keep track of the largest result.
'''

class Solution:
    def findLengthOfLCIS(self, nums: [int]) -> int:
        if len(nums) == 0:
            return 0
        return self.findHelper(nums[1:], 0, nums[0])

    def findHelper(self, nums: [int], length, curr: int) -> int:
        if len(nums) == 0:
            return length + 1
        if nums[0] > curr:
            return self.findHelper(nums[1:], length + 1, nums[0])
        return max(length + 1, self.findLengthOfLCIS(nums))


print(Solution().findLengthOfLCIS([1,3,5,4,7])) # 3
print(Solution().findLengthOfLCIS([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])) # 2


'''
Dynamic approach:
  1. Use a 1D cache of length n.
  2. Each index in this cache stores the length of the longest increasing
     subsequence ending at the index.
  3. At the end, return the largest value in this cache.
'''

class Solution:
    def findLengthOfLCIS(self, nums: [int]) -> int:
        if not nums:
            return 0
        cache = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cache[i] = cache[i-1] + 1
        return max(cache)


print(Solution().findLengthOfLCIS([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
# 2

# This reduces the time complexity to O(N^2).
# The space complexity is O(N) due to the 1D cache.


# Another solution. Reset the anchor if we break the condition
class Solution:
    def findLengthOfLCIS(self, nums: [int]) -> int:
        if not nums:
            return 0
        # start/end index
        # if increasing, result++
        ans = anchor = 0
        for i in range(len(nums)):
            # If we find a decreasing value, we have a new anchor
            if i and nums[i-1] >= nums[i]:
                anchor = i
            ans = max(ans, i - anchor + 1)
        return ans