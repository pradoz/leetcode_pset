'''
Al-Gore Rythym
1. for every number, iterate through that numbers index + i, where i are all of
    the numbers from [1,curr_number]
2. Update the minimum number of jumps at index+i
3. The min jump is that number, or that number+i
4. Make sure to see if we are out of bounds before jumping

 - Worst case runtime complexity is quadratic if we have to jump n.
 - Space complexity should be linear since we have to store all the numbers
    while we traverse the list
'''

class Solution:
    def jump(self, nums: [int]) -> int:
        jumps = [float('inf')] * len(nums)
        jumps[0] = 0

        for i, n in enumerate(nums):
            for j in range(1, n + 1):
                if i + j < len(nums):
                    jumps[i + j] = min(jumps[i + j], jumps[i] + 1)
                    print('min of:', jumps[i + j], jumps[i] + 1,'--->', min(jumps[i + j], jumps[i] + 1))
                else:
                    break
            print(jumps)

        return jumps[-1]


print(Solution().jump([3, 2, 5, 1, 1, 9, 3, 4])) # 2