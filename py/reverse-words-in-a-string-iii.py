'''
Given a string, you need to reverse the order of characters in each word within
a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
'''

# Naive/brute force solution
# Time Complexity: O(n), since work is done in a linear pass
# Space Complexity: O(n), since we store every character in the list

class Solution:
    def reverseWords(self, string_to_reverse: str) -> str:
        words = string_to_reverse.split(' ')
        reverse = ''
        for word in words:
            word = word[::-1]
            if reverse == '':
                reverse = word
            else:
                reverse += ' ' + word
        return reverse

# Less code, not much improvement.
class Solution:
    def reverseWords(self, string_to_reverse: str) -> str:
        if len(string_to_reverse) < 2:
            return string_to_reverse

        return ' '.join(word for word in string_to_reverse[::-1].split(' ')[::-1])


