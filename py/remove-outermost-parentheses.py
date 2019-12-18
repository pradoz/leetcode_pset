# uses O(n) time to iterate through every parenthesis in the string
# uses n-2 => O(n) space to construct the new sequence of parenthesis 
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result = []

        nestedCounter = 0
        for paren in S:
            if paren == '(':
                if nestedCounter > 0:
                    result.append('(')
                nestedCounter += 1
            else: # if paren == ')':
                nestedCounter -=  1
                if nestedCounter > 0:
                    result.append(')')

        return ''.join(result)