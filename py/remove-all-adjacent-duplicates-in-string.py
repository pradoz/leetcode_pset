# Time Complexity: O(n) since we have to iterate through the entire string once
# Space Complexity: O(n) since the worst case has no duplicates and we store
#                   the entire string on the stack before returning

class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []

        for ch in S:
            # if the most recent character we appended matches the character on
            # the top of the stack, then pop the character
            if stack and stack[-1] == ch:
                stack.pop()
            else: # otherwise append it to the stack
                stack.append(ch)

        return ''.join(stack)

print(Solution().removeDuplicates("abbaca")) # ca