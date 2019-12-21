# quadratic runtime, constant space
# check for a match in every possible shifted sequence for every integer up to
# the size of the strings.
class Solution1:
    def rotateString(self, A: str, B: str) -> bool:
        # trivial cases
        if A == B: # when A and B are the same string
            return True

        lengthOfA = len(A)
        lengthOfB = len(B)

        # check the different combinations of shifted sequences
        for shift in range(lengthOfA):
            check = A[shift:lengthOfA] + A[0:shift]
            if check == B: # we found a match
                return True

        # no combinations matched
        return False


# python ternary with a ternary inside
class Solution2:
    def rotateString(self, A: str, B: str) -> bool:
        return False if len(A) != len(B) else True if B in (A + A) else False

        # if len(A) != len(B):
        #     return False
        # return True if B in (A + A) else False


print(Solution().rotateString('abcde', 'cdeab')) # True
print(Solution().rotateString('abcde', 'abced')) # False