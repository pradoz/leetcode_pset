'''
ex1:
Input: "(()())(())"
Output: "()()()"

ex2:
Input: "(()())(())(()(()))"
Output: "()()()()(())"

ex3:
Input: "()()"
Output: ""
'''
# Time/Space: O(n), where n is the number of parenthesis is the string 'parens'
class Solution:
    def removeOuterParentheses(self, parens: str) -> str:
        res = ''
        prev = 0
        count = 0

        for i, s in enumerate(parens):
            if s == '(': # we have an open bracket
                count += 1 # increment count by one
            else:
                count -= 1 # if we have another closing bracket, subtract one

            # print(res)
            if count == 0: # if we opened and closed: i.e. '(' then ')'
                res += parens[prev + 1: i] # append the valid sequence to res
                # print(f'(i:{i}, s:\'{s}\') ==> res:{res}')
                prev = i + 1 # track next place for input in res

        return res

s1 = Solution()
# print(s1.removeOuterParentheses("(()())(())"))
print(s1.removeOuterParentheses("(()())(())(()(()))"))
# print(s1.removeOuterParentheses("()()"))
# assert s1.removeOuterParentheses("(()())(())") == "()()()"
# assert s1.removeOuterParentheses("(()())(())(()(()))") == "()()()()(())"
# assert s1.removeOuterParentheses("()()") == ""
