'''
Given an array nums of n integers where n > 1,  return an array output
such that output[i] is equal to the product of all the elements of nums
except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity?
'''

'''
If division was allowed:
  1. Calculate the product of all the elements in the array
  2. Do a second pass where we divide the total product by the current
     element.

Without division:
The element at index i is the product of all the numbers before i,
and all the numbers after i.

  1. Generate a list of these "prefix" and "suffix" products for
     each element.
  2. The output at each index is the product of the prefixes and suffixes
'''
# Runtime complexity is linear because the algorithm terminates in 3 passes
# Space complexity is linear because we have to store n-1 elements to calculate
#     the product at the return index.

class Solution0:
    def __init__(self):
        self.prefixes = []
        self.suffixes = []

    def get_prefix_and_suffix(self, nums: [int]) -> None:
        # Get prefix products
        for num in nums:
            if self.prefixes:
                self.prefixes.append(self.prefixes[-1] * num)
            else:
                self.prefixes.append(num)

        # Get prefix products
        for num in reversed(nums):
            if self.suffixes:
                self.suffixes.append(self.suffixes[-1] * num)
            else:
                self.suffixes.append(num)
        self.suffixes = list(reversed(self.suffixes))

        # print(self.prefixes)
        # print(self.suffixes)

    def productExceptSelf(self, nums: [int]) -> [int]:
        self.get_prefix_and_suffix(nums)
        ret = []
        for i in range(len(nums)):
            if i == 0:
                ret.append(self.suffixes[i+1])
            elif i == len(nums) - 1:
                ret.append(self.prefixes[i-1])
            else:
                ret.append(self.prefixes[i-1] * self.suffixes[i+1])
        return ret


# There was a challenge to minimize the space used
# There is a bit of complexity added to the runtime, since we pop current index
# from the list and then we insert it back at that index.
# --> We have to trust the compiler/interpreter to not resize due to the
#     removal and reinsertion etc.

# Keep a dictionary to remember what each product was with that number removed
class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        ret = []

        removed = {}
        
        for i in range(len(nums)):
            curr = nums[i]
            if curr not in removed:
                nums.pop(i)
                product = self.product(nums)
                ret.append(product)
                nums.insert(i, curr)
                removed[curr] = product
            else:
                ret.append(removed[curr])
        return ret
    
    def product(self, arr: [int]) -> int:
        result = 1
        for n in arr:
            result *= n
        return result

print(Solution().productExceptSelf([1,2,3,4]))
print(Solution().productExceptSelf([-1,-1,1,-1,-1,1,-1,-1,-1,1,1,-1,1,1,1,1,-1,1,1,-1,-1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,-1,1,1,-1,-1,1,-1,1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,-1,1,1,-1,1,1,-1,1,-1,-1,-1,1,-1,1,-1,1,1,1,1,1,-1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,1,-1,1,1,1,-1,1,1,-1,-1,1,1,-1,1,-1,1,1,-1,-1,1,-1,-1,-1,1,1,1,1,-1,1,1,-1,-1,1,1,1,-1,1,-1,1,-1,-1,1,-1,1,-1,1,-1,1,-1,1,1,1,-1,1,1,1,1,-1,-1,1,-1,1,1,1,1,1,-1,1,-1,1,-1,-1,-1,1,1,1,1,-1,-1,1,-1,-1,-1,1,1,-1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,-1,1,1,-1,1,1,-1,-1,-1,1,1,1,-1,1,-1,1,1,-1,-1,-1,-1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,1,-1,-1,1,1,-1,1,-1,1,-1,1,-1,1,-1,1,1,1,1,-1,1,-1,-1,-1,1,1,-1,1,1,1,-1,1,-1,-1,-1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,1,1,1,-1,1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,-1]))
