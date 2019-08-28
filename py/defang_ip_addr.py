from sys import getsizeof

class Solution1:
    def defangIPaddr(self, address: str) -> str:
        total = 0
        s = ''
        total += getsizeof(s)
        for c in address:
            if c != '.':
                s += c
                total += getsizeof(s)
            else: # c == '.':
                s += '[.]'
                total += getsizeof(s)
        print(f'With a string -- getsizeof(s): {total}')
        return s

class Solution2:
    def defangIPaddr(self, address: str) -> str:
        total = 0
        chars = []
        for c in address:
            if c != '.':
                chars.append(c)
            else: # c == '.':
                chars.append('[.]')
        total = getsizeof(chars) + getsizeof("".join(chars))
        print(f'With a list -- getsizeof(chars): {total}')
        return "".join(chars)

s1 = Solution1()
print(s1.defangIPaddr('1.1.1.1'))

s2 = Solution2()
print(s2.defangIPaddr('1.1.1.1'))