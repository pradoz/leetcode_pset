test = [(1, 3), (3, 4), (2, 2)]
print(test)
test.sort(key=lambda x: x[1])
print(test)