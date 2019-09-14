'''
A string S of lowercase letters is given. We want to partition this string
into as many parts as possible so that each letter appears in at most one part,
and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it
splits S into less parts.
'''
# Random question: Do all character occurence problems use dictionaries?

# Time Complexity: O(n) where n is the number of characters in S. We do all of
# the work in a linear pass
# Space Complexity: O(1) since we only need to store the alphabet and an integer
# representing each occurence.

class Solution:
    def partitionLabels(self, S: str) -> [int]:
        if not S:
            return S

        seen = {}
        for i in range(len(S)):
            char = S[i]
            if char not in seen:
                seen[char] = [i, i] # [start, end]
            else:
                seen[char][-1] = i # update end

        seen = sorted(seen.values())
        ret = []
        for span in seen:
            start, end = span
            if len(ret) == 0:
                ret.append(span)
            else:
                if ret[-1][1] > start:
                    ret[-1][1] = max(end, ret[-1][1])
                else:
                    ret.append(span)
        return [s[1] - s[0] + 1 for s in ret]


'''
Record the location of the first and last time we see each character.
'''
# Time Complexity: O(n) where n is the number of characters in S. We do all of
# the work in a linear pass
# Space Complexity: O(1) since we only need to store the alphabet and an integer
# representing each occurence.

# Similar two pointer solution. Also order n for both time and space.
class Solution:
    def partitionLabels(self, S: str) -> [int]:
        seen = {char: idx for idx, char in enumerate(S)}
        left, right = 0, 0
        ret = []

        for i, char in enumerate(S):
            right = max(right, seen[char])

            if i == right:
                span = right - left + 1
                ret.append(span)
                left = i + 1
        return ret


class Solution:
    def partitionLabels(self, S: str) -> [int]:
        ret = []
        seen = {}

        for i in range(len(S) - 1, -1, -1):
            if S[i] not in seen:
                seen[S[i]] = i

        i = 0
        span = 0
        while i < len(S):
            j = seen[S[i]] # Get the first occurence of the character

            # each sequence will have a span of one intially due to its first
            # letter
            span = 1

            # loop until the we find the second occurence
            while i != j:
                span += 1 # Keep track of the span length for each secquence
                j = max(j, seen[S[i]])
                i += 1
            ret.append(span)
            i += 1
        return ret


S = "ababcbacadefegdehijhklij"
print(Solution().partitionLabels(S))