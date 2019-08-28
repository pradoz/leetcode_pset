# hamming-distance.py
'''
The Hamming distance between two integers is the number of positions at which
the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 2^31

Example:
Input: x = 1, y = 4
Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
'''


import timeit

def hammingDistance1(x: int, y: int) -> int:
        return (bin(x ^ y)).count('1')

def hammingDistance2(x: int, y: int) -> int:
        x = bin(x)[2:]
        y = bin(y)[2:]        
        if len(x) > len(y):
            y = y.rjust(len(x), '0')
        else:
            x = x.rjust(len(y), '0')

        diff = 0
        for xbit, ybit in zip(x, y):
            if xbit != ybit: diff += 1   
        return diff

def hammingDistance3(x: int, y: int) -> int:
        xor = x ^ y
        counter = 0
        for i in range(32): # go through all bits from 2^0 up to 2^31
            if xor >> i & 1 == 1: # if that number divided by 2^i == 1
                counter += 1
        return counter

# similar to 2, less use of builtin functions
# no idea why a list is using less memory than an int
# maybe the list of characters is always less than 32, so smaller
# than largest possible int
class Solution:
    def hammingDistance4(self, x: int, y: int) -> int:
        x = bin(x)[2:]
        y = bin(y)[2:]
        
        if len(x) > len(y):
            y =  (len(x) - len(y)) * '0' + (y)
        if len(x) < len(y):
            x =  (len(y) - len(x)) * '0' + (x)
        
        a = []
        for i in range(len(x)):
            if(x[i] != y[i]):
                a.append(i)

        return len(a)


print(timeit.timeit('hammingDistance1(500, 42032)', globals=globals()))
print(timeit.timeit('hammingDistance2(500, 42032)', globals=globals()))
print(timeit.timeit('hammingDistance3(500, 42032)', globals=globals()))




