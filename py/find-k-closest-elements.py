# O(log(n) + k) time
# O(1) space
class Solution0:
    def findClosestElements(self, arr: [int], k: int, x: int) -> [int]:
        left = 0
        right = len(arr) - k

        while left < right:
            mid = left + (right - left) // 2

            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left : left + k]


# max heap
# uses O(k) space
from heapq import heappush, heappushpop

class Solution:
    def findClosestElements(self, arr: [int], k: int, x: int) -> [int]:
        kClosest = []

        for num in arr:
            if len(kClosest) == k:
                heappushpop(kClosest, (-abs(x - num), -num))
            else:
                print(num, '----', (-abs(x - num), -num))
                heappush(kClosest, (-abs(x - num), -num))

        return sorted([-tup[1] for tup in kClosest])


lst = [1,2,3,4,5]
print(Solution().findClosestElements(lst, 4, 3))
# 1 2 3 4

