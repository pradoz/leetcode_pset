# Needs an up and down point since A.length >= 3
# 3 <= A.length <= 10000
# Given an array that is definitely a mountain,
# return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]

# Time Complexity: O(n), worst case visits every element in the list
# Space Complexity: O(1), we don't store anything. search is done in-place

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        for n in range(len(A)-1):
            if A[n] > A[n+1]:
                return n

# Time Complexity: O(log n), worst case visits log n elements (binary search)
# Space Complexity: O(1), we don't store anything. search is done in-place

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        front = 0
        back = len(A) - 1
        while front < back:
            mid = (back + front) / 2
            if A[mid] < A[mid+1]:
                front = mid + 1
            else:
                back = mid
        return front

# Built-in function, returns the index of the max element in the list
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return A.index(max(A))
