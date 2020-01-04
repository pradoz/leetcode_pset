# Implement a basic calculator to evaluate a simple expression string.

# The expression string may contain open ( and closing parentheses ),
# the plus + or minus sign -, non-negative integers and empty spaces .

# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.

class Solution:
    def calculate(self, expression: str) -> int:
        result = 0
        index = 0
        expSize = len(expression)

        operator = [1, 1]

        expression.strip() # remove outer whitespace

        while index < expSize:
            symbol = expression[index]
            if symbol.isdigit():
                start = index
                while index < expSize and expression[index].isdigit():
                    index += 1
                result += operator.pop() * int(expression[start:index])
                continue
            if symbol in ('+', '-', '('):

                # operator is negative if symbol == '-', plus otherwise
                trueIfPlus_minusIfFalse = symbol == '-'
                operator += operator[-1] * (1, -1)[trueIfPlus_minusIfFalse],
            elif symbol == ')':
                operator.pop()
            index += 1
        return result















print(Solution().calculate("1 + 1")) # 2
print(Solution().calculate(" 2-1 + 2 ")) # 3
print(Solution().calculate("(1+(4+5+2)-3)+(6+8)")) # 23
print(Solution().calculate('(1 + (2 + (3 + (4 + 5))))')) # 15
print(Solution().calculate('2147483647')) # 2147483647
print(Solution().calculate('  30')) # 30
print(Solution().calculate('1-11')) # -10