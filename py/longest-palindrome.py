import collections


'''
idea:
return the sum of the appearances of characters if they are even. if there are
any values of odd occurences, we need to them.
'''

# using less built-ins than other soltuions.
class Solution:
    def longestPalindrome(self, s: str) -> int:
        # these two operations for 'freq' could replace the 'freq={}'
        # declaration and construction inside the for loop.
        # freq = collections.Counter()
        # freq.update(s)
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        # We only need odd, if it exists
        added_an_odd_freq = False
        length_of_longest_palindrome = 0
        for val in freq.values():
            if val % 2 == 0:
                length_of_longest_palindrome += val
            elif not added_an_odd_freq:
                length_of_longest_palindrome += val
                added_an_odd_freq = True
            else:
                length_of_longest_palindrome += val - 1
        # print(freq)
        # print(length_of_longest_palindrome)
        return length_of_longest_palindrome





# pythonic solution
class Solution1:
    def longestPalindrome(self, s: str) -> int:
        counts = collections.Counter(s).values()
        use = sum(v & ~1 for v in counts) + any(v & 1 for v in counts)
        # print(use)

        # print(list(v & ~1 for v in counts))

        return use


        

print(Solution().longestPalindrome("abccccdd")) # 7