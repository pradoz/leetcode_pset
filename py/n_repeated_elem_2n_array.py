# n_repeated_elem_2n_array.py
'''
In a array A of size 2N, there are N+1 unique elements, and exactly one of
these elements is repeated N times. Return the element repeated N times.

Example 1:
Input: [1,2,3,3]
Output: 3

Example 2:
Input: [2,1,2,5,3,2]
Output: 2

Example 3:
Input: [5,1,5,2,5,3,5,4]
Output: 5

Note:
4 <= A.length <= 10000
0 <= A[i] < 10000
A.length is even
'''
from sys import getsizeof

# using a set was faster than a list, but used more memory
class Solution1:
    def repeatedNTimes(self, A: [int]) -> int:
        seen = set()
        for num in A:
            if num in seen:
                return num
            else:
                seen.add(num)

# using a list was less space than a set
class Solution2:
    def repeatedNTimes(self, A: [int]) -> int:
        num_list = []
        for num in A:
            if num in num_list:
                # print(getsizeof(num_list))
                return num
            num_list.append(num)

# memory efficient solution (slow)
# idea: use given constraint to avoid resizing the list
# [2,1,2,5,3,2]
class Solution3:
    def repeatedNTimes(self, A: [int]) -> int:
        # store a list with a count for every possible number
        options = [0 for x in range(10000)]
        print(getsizeof(options))

        for x in A:
            options[x] += 1

        i_max = 0
        count_max = 0

        # traverse the indexes, count max reoccurences
        for idx, count in enumerate(options):
            if count > count_max:
                count_max = count
                i_max = idx
        return i_max

# solution using map (incredibly slow)
class Solution:
    def repeatedNTimes(self, A: [int]) -> int:
        unique_nums = set(A)
        list(map(A.remove, unique_nums))
        return A[0]





s1 = Solution()
print(s1.repeatedNTimes([1,2,3,3]))
print(s1.repeatedNTimes([2,1,2,5,3,2]))