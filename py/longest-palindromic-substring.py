class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s

        bestString = ''
        bestLength = 0

        for i in range(size):
            # odd case
            checkString = self.getPalindrome(s, i, i, size)
            checkLength = len(checkString)
            if checkLength > bestLength:
                bestString = checkString
                bestLength = checkLength

            # even case
            checkString = self.getPalindrome(s, i, i + 1, size)
            checkLength = len(checkString)
            if checkLength > bestLength:
                bestString = checkString
                bestLength = checkLength

        return bestString

    def getPalindrome(self, s: str, left, right, size: int) -> str:
        while left >= 0 and right < size and s[left] == s[right]:
            left -= 1 # move left
            right += 1 # move right
        return s[left + 1 : right]


print(Solution().longestPalindrome("cbbd")) # bb
print(Solution().longestPalindrome("ccd")) # cc
print(Solution().longestPalindrome("bacaba")) # bacab
print(Solution().longestPalindrome("abacaba")) # abacaba
print(Solution().longestPalindrome("a")) # a
print(Solution().longestPalindrome("ccc")) # ccc
print(Solution().longestPalindrome("xx")) # xx
print(Solution().longestPalindrome("abacab")) # bacab