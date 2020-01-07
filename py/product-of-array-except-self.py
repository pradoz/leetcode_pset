class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        sizeOfNums = len(nums)
        result = []

        product = 1

        # get right-side product
        for i in range(sizeOfNums):
            result.append(product)
            product *= nums[i]
            # print("i:", i, "product:", product, "nums:", nums, "result:", result)

        product = 1

        # print("product:", product, "nums:", nums, "result:", result)
        # get left-side product
        for i in range(sizeOfNums-1, -1, -1):
            result[i] *= product
            product *= nums[i]
            # print("i:", i, "product:", product, "nums:", nums, "result:", result)

        return result





print(Solution().productExceptSelf([1,2,3,4])) # [24,12,8,6]