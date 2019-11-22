# recursive
class Solution0:
    def searchRange(self, nums: [int], target: int) -> [int]:
        first = self.binarySearch(nums, 0, len(nums)-1, target, True)
        last = self.binarySearch(nums, 0, len(nums)-1, target, False)
        return [first, last]

    def binarySearch(self, arr: [int], low, high, target: int, findFirst: bool) -> int:
        if high < low:
            return -1

        mid = (high + low) // 2

        if findFirst == True:
            if (mid == 0 or target > arr[mid - 1]) and arr[mid] == target:
                return mid
            elif target > arr[mid]:
                return self.binarySearch(arr, mid + 1, high, target, findFirst)
            else: # target < arr[mid]:
                return self.binarySearch(arr, low, mid - 1, target, findFirst)
        else: # if we are the recursive call from "last"
            if (mid == len(arr) - 1 or target < arr[mid + 1]) and arr[mid] == target:
                return mid
            elif target < arr[mid]:
                return self.binarySearch(arr, low,  mid - 1, target, findFirst)
            else: # target > arr[mid]:
                return self.binarySearch(arr, mid + 1, high, target, findFirst)

# Iterative, change recursive calls to modify the parameters within a loop
class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        first = self.binarySearch(nums, 0, len(nums)-1, target, True)
        last = self.binarySearch(nums, 0, len(nums)-1, target, False)
        return [first, last]

    def binarySearch(self, arr: [int], low, high, target: int, findFirst: bool) -> int:
        while True:
            if high < low:
                return -1

            mid = (high + low) // 2

            if findFirst == True:
                if (mid == 0 or target > arr[mid - 1]) and arr[mid] == target:
                    return mid
                elif target > arr[mid]:
                    low = mid + 1
                else: # target <= arr[mid]:
                    high = mid - 1
            else: # if we are the recursive call from "last"
                if (mid == len(arr) - 1 or target < arr[mid + 1]) and arr[mid] == target:
                    return mid
                elif target < arr[mid]:
                    high = mid - 1
                else: # target >= arr[mid]:
                    low = mid + 1



arr = [0] * 100
# arr = [1,3,3,5,7,8,9,9,154,6,8,9,9,9,3,4]
target = 0
print(Solution().searchRange(arr, target))