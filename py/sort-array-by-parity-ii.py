# In place, minimizing total allocations and iterations

# Invariant:
# arr[i] is an even number at even index and
# arr[j] is an odd number at odd index.
# As soon as this invariant is violated, we can swap numbers to restore it.

class Solution:
    def sortArrayByParityII(self, arr: [int]) -> [int]:
        j = 1
        for i in range(0, len(arr), 2):
            if arr[i] % 2 == 1:
                while arr[j] % 2 == 1:
                    j += 2
                arr[i], arr[j] = arr[j], arr[i]
        return arr


# Naive solution runs in O(n), creating a new array O(n) -> space
class Solution0:
    def sortArrayByParityII(self, arr: [int]) -> [int]:
        res = [0] * len(arr)

        even_idx = 0
        odd_idx = 1

        for x in arr:
            if x % 2 == 0:
                res[even_idx] = x
                even_idx += 2
            else:
                res[odd_idx] = x
                odd_idx += 2
        return res


# Naive solution runs in O(n), done in place O(1) -> space
class Solution1:
    def sortArrayByParityII(self, arr: [int]) -> [int]:
        even_idx = 0
        odd_idx = 1
        sz = len(arr)

        while even_idx < sz and odd_idx < sz:
            if arr[even_idx] % 2 == 0:
                even_idx += 2
            elif arr[odd_idx] % 2 == 1:
                odd_idx += 2
            else:
                # arr[even_idx] % 2 == 1 and arr[odd_idx] % 2 == 0

                # swap the mismatched indexes
                arr[even_idx], arr[odd_idx] = arr[odd_idx], arr[even_idx]
                even_idx += 2
                odd_idx += 2
        return arr



print(Solution().sortArrayByParityII([4,2,5,7]))