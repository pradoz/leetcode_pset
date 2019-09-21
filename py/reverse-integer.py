'''
1. Get the parity of x
2. Take absolute value of x
3. Convert x to a string
4. Reverse the string
5. Convert the string back to an integer
6. Reapply the sign from earlier
7. Check if in range:
    If it is in range, return the number
    If not return 0
'''

# Runs in linear time as we need to convert every digit to a string, apply
# linear functions to them, and convert every character back to a digit.

# The built in reverse uses linear extra space to construct the new string. We
# can write it in place to reduce memory used, but still need to store the entire
# string.

# In place reverse string without build in reverse
class Solution:
    def reverse(self, x: int) -> int:
        # Get the parity of x
        # sign = [1, -1][x < 0]
        if x < 0:
            sign = -1
        else:
            sign = 1

        # Get the absolute value of x, convert it to a string, split each char
        # to an index in a list
        x_str = list(str(abs(x)))

        # Reverse the string
        size = len(x_str)
        for i in range(size//2):
            x_str[i], x_str[size - i - 1] = x_str[size - i - 1], x_str[i]

        # Apply the sign from earlier and convert the string back to an int
        reversed_int = sign * int(''.join(x_str))

        if (-(2**31) - 1 < reversed_int < 2**31):
            return reversed_int
        return 0


class Solution0:
    def reverse(self, x: int) -> int:
        # Get the parity of x
        if x < 0:
            sign = -1
        else:
            sign = 1

        # Get the absolute value of x, convert it to a string, and reverse it
        x_as_a_string = str(abs(x))[::-1]

        # Apply the sign from earlier and convert the string back to an int
        reversed_int = sign * int(x_as_a_string)

        if (-(2**31) - 1 < reversed_int < 2**31):
            return reversed_int
        return 0


# Slightly more efficient solution with a list
class Solution1:
    def reverse(self, x: int) -> int:
        x_list = list(str(abs(x)))
        x_list.reverse()
        reversed_int = int(''.join(x_list))

        # Apply parity from the original x value
        if x < 0:
            reversed_int *= -1

        # Check if the integer is in the valid range
        if (-(2**31) - 1 < reversed_int < 2**31):
            return reversed_int
        return 0


print(Solution().reverse(123)) # 321
print(Solution().reverse(2**31)) # 0