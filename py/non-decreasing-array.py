class Solution:
    def checkPossibility(self, nums: [int]) -> bool:
        shiftCount = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                shiftCount += 1

                if shiftCount > 2:
                    return False

                if i < 2 or nums[i - 2] <= nums[i]:
                    print("nums[i - 1] = nums[i]")
                    nums[i - 1] = nums[i]
                else:
                    print("nums[i] = nums[i - 1]")
                    nums[i] = nums[i - 1]

        print(shiftCount)
        return shiftCount < 2




print(Solution().checkPossibility([4,2,3])) # True
print(Solution().checkPossibility([4,2,1])) # False
print(Solution().checkPossibility([3,4,2,3])) # False
print(Solution().checkPossibility([-1,4,2,3])) # True