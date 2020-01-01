# Write two functions that return true if there exists numbers a, b, and c such
# that a, b, and c are pythagorean triplets.

# 1. optimize for space
# 2. optimize for time

def findPythagoreanTriplets1(nums: [int]) -> bool:
    for a in nums:
        for b in nums:
            for c in nums:
                if a ** 2 + b ** 2 == c ** 2:
                    return True
    return False


# generates a list of squares to check to avoid the triple nested loop
def findPythagoreanTriplets2(nums: [int]) -> bool:
    listOfSquares = set([n ** 2 for n in nums])

    for a in nums:
        for b in nums:
            if a ** 2 + b ** 2 in listOfSquares:
                return True
    return False




print(findPythagoreanTriplets1([3, 5, 12, 5, 13])) # True
print(findPythagoreanTriplets2([3, 5, 12, 5, 13])) # True