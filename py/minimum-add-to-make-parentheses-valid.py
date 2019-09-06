'''
Given a parentheses string, return the minimum number of parentheses we
must add to make the resulting string valid.


Example 1:
Input: "())"
Output: 1

Example 2:
Input: "((("
Output: 3
'''

# Time Complexity: O(n) since we iterate through the entire string once.
# Space Complexity: O(1) since everything is done in-place

# keeping track of left and right
class Solution:
    def minAddToMakeValid(self, string: str) -> int:
        left, right = 0, 0
        for char in string:
            if char == '(':
                left += 1
            elif left > 0:
                left -= 1
            else:
                right += 1
        return left + right


# keeping track of opened sequences
class Solution:
    def minAddToMakeValid(self, string: str) -> int:
        opened = 0
        invalid = 0
        for c in string:
            if c == '(':
                opened += 1
            elif c == ')':
                if opened > 0:
                    opened -= 1
                else:
                    invalid += 1

        invalid += opened
        return invalid


# This COULD be an efficient solution if the string is guaranteed small.
# Time Complexity: O(n) since we iterate through the entire string once.
# Space Complexity: O(m) where m is the number of open parenthesis.
class Solution:
    def minAddToMakeValid(self, string: str) -> int:
        stack = []
        count = 0
        for char in string:
            if char == '(':
                stack.append(char)
            elif c == ')':
                if len(stack) > 0:
                    stack.pop()
                else:
                    count += 1
        return count + len(stack)