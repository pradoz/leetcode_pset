'''
Solution Explanation:
First we should sort nums, iterate through every number in nums, using the
current number as a target value which can be reached obtaining a larger or
smaller number by incrementing the left pointer or decrementing the right
pointer, respectively.


Complexity:
The main part of the algorithm runs in O(n^2 + n*logn), and since .sort() runs
in-place (uses no extra space), and has runtime complexity O(n*logn) which is
much smaller than n^2, Big-Oh is asymptotic so the n^2 will dominate here.
We use n extra space because in the worst case (where no 3 sum exists) we would
have to store every number in nums. 

Time Complexity: O(n^2)
Space Complexity: O(n)
'''

class Solution(object):
    def threeSum(self, nums: [int]) -> [[int]]:
        results = []
        nums.sort()
        size = len(nums)

        # Exit early cases:
        # 1. If the list has less than 3 elements.
        # 2. If the first element is positive in an increasingly sorted list,
        #    then their sum will always be greater than zero.
        # 3. If the last element is negative in the increasingly sorted list,
        #    then we have the converse of case 2.
        if size == 0 or nums[0] > 0 or nums[-1] < 0:
            return []

        # This algorithm requires at least 3 elements to continue
        for i in range(size - 2):
            # We don't need to check duplicate elements, "continue" takes us
            # back to the top of the loop body.
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Left and right pointers
            left = i + 1
            right = size - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                # If the total is less than zero, we need to move the left
                # pointer to the right to get a larger number.
                if total < 0:
                    left += 1

                # If the total is greater than zero, we need to move the right
                # pointer to the left to get a smaller number.
                elif total > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return results
