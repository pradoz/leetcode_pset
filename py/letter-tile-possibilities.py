# Using DFS
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        seen = set()
        def dfs(curr_key, s: str) -> None:
            if curr_key in seen:
                return 
            seen.add(curr_key)

            for i, e in enumerate(s):
                dfs(curr_key + e, s[:i] + s[i+1:])
            return 
        # Sorting the string lets us skip operations on duplicate permutations
        # when we backtrack
        dfs("", sorted(tiles))
        return len(seen) - 1 # remove the empty string


# Using a collection and math
from collections import Counter
from math import factorial
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # Get the frequencies of different characters
        char_frequency = Counter(tiles)
        prod = 1
        for freq in char_frequency.values():
            prod *= freq + 1

        # For permutations with repetition:
        # [i_0, i_1, ..., i_n] (0 <= i_k <= f_k, k = 0, 1, ..., n),
        # the number of distinct sequences is:
        # (i_0 + i_1 + ... + i_n)! / ( i_0! * i_1! * ... * i_n!)
        res = 0
        for i in range(1, prod):
            nums = []
            for freq in char_frequency.values():
                nums.append(i % (freq + 1))
                i = i // (freq + 1)
            curr = factorial(sum(nums))
            for num in nums:
                curr //= factorial(num)
            res += curr
        return res



tiles = "AAB"
print(Solution().numTilePossibilities(tiles))
# tiles = "AAABBC"
# print(Solution().numTilePossibilities(tiles))