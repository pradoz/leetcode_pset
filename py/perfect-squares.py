# runtime complexity is O(n * sqrt(n)) = O(n^(3/2)) since we iterate up to the
# square root of n for every n elements

# space complexity is n+sqrt(n), which simplifies to O(n), to construct the
# list of minSums and squares

class Solution:
    def numSquares(self, n: int) -> int:
        squaresLessThanN = [x ** 2 for x in range(1, n+1) if x ** 2 <= n]
        print(squaresLessThanN)

        minSums = [n] * (n + 1)
        minSums[0] = 0 # sum zero is irrelevant

        for nextBiggestSquare in range(len(minSums)):
            for square in squaresLessThanN:
                # print(f'''currSum: {currSum}, nextBiggestSquare: {nextBiggestSquare}, square: {square}
                #     -- minSums: {minSums}''')

                currSum = nextBiggestSquare + square
                if currSum < len(minSums):
                    minSums[currSum] = min(minSums[currSum], \
                                           minSums[nextBiggestSquare] + 1)

        return minSums[-1]








# print(Solution().numSquares(13))
# print(Solution().numSquares(12))
print(Solution().numSquares(4))