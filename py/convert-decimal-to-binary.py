# Given a non-negative integer n, convert n to base 2 in string form.
# Do not use any built in base 2 conversion functions like bin.

def base_2(n: int) -> str:
    ret = []
    radix = 2


    # we are done converting to binary when n=0
    while n > 0:
        bit = n % radix # get the next bit
        ret.append(str(bit)) # add the bit to the list
        n //= radix # divide by the radix

    # return the reversed bits, since we have MSB
    return ''.join(reversed(ret))




print(base_2(123))
# 1111011

# In the above example, 2^6 + 2^5 + 2^4 + 2^3 + 2^1 + 2^0 = 123.