# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it is able to trap after raining.

# The above elevation map is represented by array:
# [0,1,0,2,1,0,1,3,2,1,2,1]
# In this case, 6 units of rain water (blue section) are being trapped.

# Example:
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
class Solution0:
    def trap(self, heights: [int]) -> int:
        i = 0
        j = len(heights) - 1
        max_left = 0
        max_right = 0
        area = 0

        while i < j:
            max_left = max(max_left, heights[i])
            max_right = max(max_right, heights[j])
            if max_left > max_right:
                area += max_right - heights[j]
                j -= 1
            else:
                area += max_left - heights[i]
                i += 1
        return area

# without max function
class Solution:
    def trap(self, heights: [int]) -> int:
        if len(heights) < 3:
            return 0
        left, right = 0, len(heights) - 1

        total = 0
        max_left = 0
        max_right = 0

        while left <= right:
            highest_left, highest_right = heights[left], heights[right]
            if highest_left < highest_right:
                if max_left < highest_left:
                    max_left = highest_left
                else:
                    total += max_left - highest_left
                left += 1
            else:
                if max_right < highest_right:
                    max_right = highest_right
                else:
                    total += max_right - highest_right
                right -= 1

        return total

class Solution1:
    def trap(self, heights: [int]) -> int:
        n = len(heights)
        left_maxes = [0] * n
        right_maxes = [0] * n

        current_left_max = 0
        for i in range(n):
            current_left_max = max(current_left_max, heights[i])
            left_maxes[i] = current_left_max

        current_right_max = 0
        for i in range(n-1, -1, -1):
            current_right_max = max(current_right_max, heights[i])
            right_maxes[i] = current_right_max
        total = 0
        for i in range(n):
            total += min(left_maxes[i], right_maxes[i]) - heights[i]
            print(f'i={i} - left_maxes[i]: {left_maxes[i]} | right_maxes[i]: {right_maxes[i]} | heights[i]: {heights[i]}')
        print(f'left_maxes: {left_maxes} | ')
        print(f'right_maxes: {right_maxes} | ')
        return total


print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
