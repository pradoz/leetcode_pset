# O(n) runtime to iterate through every num in nums and find the result
# O(n) space to create the map for (n/2)-1 values, which asymptotically
#   appoaches n as the function grows.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}

        for num in nums:
            if num not in seen:
                seen[num] = True # sets to true after the first occurrence
            else:
                seen[num] = False # sets to false after the duplicate occurrs

        # result = 0

        for key, val in seen.items():
            if val == True:
                return key




# O(n) runtime to iterate through every num in nums
# O(1) space
## using XOR: all of the bits will be flipped to zero if a number is XOR'd with
#             itself. this means that the last bits will be flipped on for the
#             non-duplicate value since it any set of bits B XOR'd with all 0
#             bits will give you back the same set of bits B.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            result ^= num

        return result