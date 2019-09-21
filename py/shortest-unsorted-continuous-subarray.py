'''
Given an integer array, you need to find one continuous subarray that if you
only sort this subarray in ascending order, then the whole array will be sorted
in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5

Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the
whole array sorted in ascending order.
'''

'''
1. iterating left to right:
    - keep track of the maximum number
    - if the numbers that follow are smaller than the largest number, then
      sort those numbers so that right is set to that index at that point.

2. iterating right to left:
    - keep track of the minimum number
    - if the numbers that follow are greater than the smallest number, then
      those numbers need to be sorted so that left is set to that index at that
      point
'''

# Runs in O(n) since two traversals are required to process it all
# Uses O(1) "constant" space to store 2 integers and two floats

class Solution0:
    def findUnsortedSubarray(self, nums: [int]) -> int:
        # It's possible to use O(n) space to check a sorted list here
        start = 0
        finish = 0
        max_num = float('-inf')
        min_num = float('inf')

        for i in range(len(nums)):
            max_num = max(max_num, nums[i])
            if nums[i] < max_num:
                finish = i

        for i in range(len(nums)-1, -1, -1):
            min_num = min(min_num, nums[i])
            if nums[i] > min_num:
                start = i
        # print(finish, start)
        if finish == start == 0:
            return 0
        return (finish - start + 1)


# One pass solution (with two pointers, so there are still the same amount of
# array lookups as the two pass algorithm)
# Still linear runtime and constant space.
class Solution:
    def findUnsortedSubarray(self, nums: [int]) -> int:
        start = 0
        finish = -1
        max_num = float('-inf')
        min_num = float('inf')

        left = 0
        right = len(nums) - 1
        while right >= 0:
            max_num = max(max_num, nums[left])
            if nums[left] != max_num:
                finish = left

            min_num = min(min_num, nums[right])
            if nums[right] != min_num:
                start = right

            left += 1
            right -= 1
        return (finish - start + 1)

        

print(Solution().findUnsortedSubarray([1,2,3,4])) # 0
print(Solution().findUnsortedSubarray([1, 7, 9, 5, 7, 8, 10])) # 5
print(Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])) # 5