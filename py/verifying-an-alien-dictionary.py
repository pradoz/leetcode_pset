'''
Given a sequence of words written in the alien language, and the order of the
alphabet, return true if and only if the given words are sorted lexicographicaly
in this alien language.

Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.


Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1],
hence the sequence is unsorted.
'''

'''
Solution Explanation:
    1. use a dictionary to create a mapping for each characters index in the
      ordered sequence.
    2. for each word, convert it to a list of ordered characters.
    3. traverse each word and compare their letter indexing to make sure it is
      in increasing order.
'''


# Time Complexity: O(n*m), where n is the number of words, and m is the length
#                     length of the longest word of all n words.
# Space Complexity: O(1), this is constant because we only need to store ar
#                     mapping from each element to its corresponding index.

class Solution0:
    def isAlienSorted(self, words: [str], order: str) -> bool:
        ordered_mapping = {char: idx for idx, char in enumerate(order)}

        # All words of length 1 or less are already sorted, return True
        if len(words) <= 1:
            return True

        last_word = [ordered_mapping[c] for c in words[0]]

        for word in words[1:]:
            new_word = [ordered_mapping[c] for c in word]
            if last_word > new_word:
                return False
            last_word = new_word

        # if the ordered mapping is always increasing, we can return True
        return True


# In-place solution (constant space used for the alphabet list instead of dict)
class Solution:
    def isAlienSorted(self, words: [str], order: str) -> bool:
        index_of_words = [c for c in order]
        for word in range(len(words) - 1):
            curr_letter = 0
            while curr_letter != len(words[word]):
                if curr_letter == len(words[word + 1]):
                    return False

                curr_word = words[word][curr_letter]
                next_word = words[word+1][curr_letter]

                if curr_word == next_word:
                    curr_letter += 1
                else:
                    if index_of_words.index(curr_word) < index_of_words.index(next_word):
                        break
                    else:
                        return False
        return True

# Super Pythonic solution
class Solution2:
    def isAlienSorted(self, words: [str], order: str) -> bool:
        ordered_mapping = {char: idx for idx, char in enumerate(order)}

        index_of_words = [[ordered_mapping[c] for c in word] \
                           for word in words]

        return all(word1 <= word2 for word1, word2 in zip(index_of_words, index_of_words[1:]))


# Test cases
print(Solution().isAlienSorted(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba"))
# False

print(Solution().isAlienSorted(["zyxz", "zyxw", "zyxwy"], "zyxwvutsrqponmlkjihgfedcba"))            
# True