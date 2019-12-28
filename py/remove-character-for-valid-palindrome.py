# O(n log n) time since we do a binary search for every character n in the
#   palindrome.
# O(1) space since we just do array lookups and store a few integers.


def isPalindrome(palindrome: str, low, high: int) -> bool:
    """ returns true if a palindrome exists from palindrome[low] to
    palindrome[high] and false otherwise """
    while low < high:
        if palindrome[low] != palindrome[high]:
            return False

        low += 1
        high -= 1
    return True

def createPalindrome(palindrome: str) -> bool:
    """ returns true if we can create a palindrome by removing a nonmatching
    character at some indexes passed to isPalindrome """
    low = 0
    high = len(palindrome) - 1

    while low < high:
        if palindrome[low] == palindrome[high]:
            low += 1
            high -= 1
        else:
            #  check for a vlid palindrome with a removed character
            return isPalindrome(palindrome, low + 1, high) or \
                   isPalindrome(palindrome, low, high - 1)
        return True









print(createPalindrome("abcdcbea")) # True
print(createPalindrome("abccba")) # False
print(createPalindrome("abccaa")) # False