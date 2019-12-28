lst = list(range(1,100))
total = 0
for i in lst:
    # get any odd number since there can be at most one odd number
    if i & ~1:
        total += i
        print(i)

print(5 // 3)