'''
Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".
'''

# Time/Space: O(n) for both. n is the sum of all word lengths

## Strategy:
# 1. Translate every string by finding its index in morse code. Store them in a list.
# 2. Cast the list into a set to get unique elements and take the length of that set.
class Solution:
    def uniqueMorseRepresentations(self, words: [str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",\
                      "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-",\
                      "...-",".--","-..-","-.--","--.."]
        s = set()
        for word in words:
            encoded = []
            for c in word:
                encoded.append(morse_code[ord(c) - ord('a')])
            s.add(''.join(encoded))
        return len(s)

# # Alternative two-liner
# lookup = {["".join(morse_code[ord(c) - ord('a')] for c in word) for word in words]}
#     return len(lookup)

# Dictionary alternative, better speed but more space needed to store the dict
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        d = dict()
        for i in range(len(alphabet)):
            d[alphabet[i]] = morse[i]
        s = set()
        for word in words:
            wordset = set(word)
            for letter in wordset:
                word = word.replace(letter, d[letter])
            s.add(word)
        return len(s)