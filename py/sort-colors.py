'''
Given an array with n objects colored red, white or blue, sort them in-place
so that objects of the same color are adjacent, with the colors in the order
red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white,
and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
'''


# Two pass solution using an array to count the occurences on the first pass.
# The second pass will reconstruct the new array we wish to return.

# Time Complexity: 2n passes implies this algorithm runs in O(n)
# Space Complexity: O(k), where k is the # of colors we store in color_dict
class Solution0:
    def sortColors(self, nums: [int]) -> None:
        """ Do not return anything, modify nums in-place instead. """
        c0 = c1 = c2 = 0
        for num in nums:
            if num == 0:
                c0 += 1
            elif num == 1:
                c1 += 1
            else:
                c2 += 1
        nums[:c0] = [0] * c0
        nums[c0:(c0 + c1)] = [1] * c1
        nums[c0+c1:] = [2] * c2



# Single pass solution using a left and right pointer

# Time Complexity: a single pass implies this algorithm runs in O(n)
# Space Complexity: O(k), where k is the constant # of colors we must store
class Solution:
    def sortColors(self, nums: [int]) -> None:
        left = curr = 0
        right = len(nums) - 1

        while curr <= right:
            if nums[curr] == 0:
                # Swap left and curr indexes
                nums[left], nums[curr] = nums[curr], nums[left]

                # Advance pointers
                left += 1
                curr += 1
            elif nums[curr] == 2:
                # Swap right with curr
                nums[curr], nums[right] = nums[right], nums[curr]

                # Decrease right hand side pointer
                right -= 1
            else: # If nums[curr] == 1
                curr += 1

nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
nums = [0]

print("Before Sort: ")
print(nums)
# [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

Solution().sortColors(nums)
print("After Sort: ")
print(nums)
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]