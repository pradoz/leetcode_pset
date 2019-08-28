def fact(k):
    if k == 0:
        return 1
    return k * fact(k-1)
print(fact(6))

def pow(k):
    if k == 0:
        return 1
    return 2 * pow(k-1)
print(pow(6))



# pow(4) = 2 * 8 = 16
#     ^
#     |
# pow(3) = 2 * 4 = 8
#     ^
#     |
# pow(2) = 2 * 2 = 4
#     ^
#     |
# pow(1) = 2 * 1 = 2
#     ^
#     |
# pow(0) = 1
# --> since k = 0, line 8 returns 1 for pow(k=0)

def iter_pow(k):
    loop_count = 0
    total = 1
    while k > 0:
        total = total * 2
        k = k - 1
        loop_count += 1
        print(f'After loop #{loop_count}, total=2^{loop_count}={total}')
iter_pow(6)