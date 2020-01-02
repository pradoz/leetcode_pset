# Time and space complexity are both O(log n). (possibly log base 16 ??)
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'

        # handle two's complement for negative values
        if num < 0:
            num = num + (2 ** 32)

        digits = '0123456789abcdef'

        result = []

        while num > 0:
            result.append(str(digits[num % 16])) # get next digit
            num //= 16                           # divide by radix 16
        return ''.join(list(reversed(result)))   # reverse digits before return

s = Solution()
print(s.toHex(5))
print(s.toHex(24))
print(s.toHex(-1))
print(s.toHex(0))
print(s.toHex(-10))