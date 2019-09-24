'''
  case 1. If we find a letter, add it to the result string.
  case 2. If we find a number, then decode that part of the string until
           find a closing bracket.

Al Gore Rythym For Parsing:
  1. parse the number for the first open bracket
  2. keep track of the bracket count until we find the matching closing bracket
  3. recursively solve that string bycalling decodeString again
  4. The resulting string returned is multiplied by the number of times
    specified and added to the result string
'''
'''
Time Complexity: O(n) since we do the work in a linear pass while constructing
    a string.
Space Complexity: O(n*k) for each set of n characters nested inside a bracket
    with k outside of the bracket.
'''
class Solution0:
    def decodeString(self, s: str) -> str:
        res = ''
        i = 0

        while i < len(s):
            if s[i].isalpha():
                res += s[i]
                i += 1
                continue

            if s[i].isdigit():
                num = 0

                # get all the numbers
                while s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1

                # parse the string inside the bracket
                bracket_count = 1
                i += 1
                inner = ''
                while bracket_count > 0:
                    if s[i] == '[':
                        bracket_count += 1
                    elif s[i] == ']':
                        bracket_count -= 1
                    inner += s[i]
                    i += 1

                # append the parsed expression and continue decoding
                res = res + num * self.decodeString(inner[:-1])
        return res



# With a list to hold the string
class Solution:
    def decodeString(self, s: str) -> str:
        decoded_str_list = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                j = i + 1

                # Get the length of the the current nested string
                while s[j] != '[':
                    j += 1

                # Get the length of the current string
                k = int(s[i:j])
                i = j + 1
                j = i

                # Track the brackets
                bracket_count = 1
                while True:
                    if s[j] == '[':
                        bracket_count += 1
                    elif s[j] == ']':
                        bracket_count -= 1

                    if bracket_count == 0:
                        break
                    else:
                        j += 1
                decoded_str_list.append(self.decodeString(s[i: j]) * k)
                i = j + 1
            else:
                decoded_str_list.append(s[i])
                i += 1
        return ''.join(decoded_str_list)


# With a stack
class Solution():
    def decodeString(self, s: str) -> str:
        stack = []
        k = 0
        curr_str = ''
        
        for c in s:
            if c == '[':
                stack.append(curr_str)

                # Keep track of k
                stack.append(k)
                curr_str = ''
                k = 0
            elif c == ']':
                # Pop k off the stack
                num = stack.pop()
                prev_str = stack.pop()
                curr_str = prev_str + num * curr_str
            elif c.isdigit():
                k = k*10 + int(c)
            else: # We have a normal character
                curr_str += c
        return curr_str


strings = [
    "2[a2[b]c]",     # abbcabbc
    "3[a]2[bc]",     # aaabcbc
    "3[a2[c]]",      # accaccacc
    "2[abc]3[cd]ef", # abcabccdcdcdef
    ]

for s in strings:
    print(Solution().decodeString(s))