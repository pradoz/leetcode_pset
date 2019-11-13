from collections import defaultdict

# O(n) time and space to preprocess the magazine
# O(m) time to check if each character occurence is inside of ransomNote
# Time complexity is O(n + m) to traverse the ransomNote and magazine each once
# Space complexity is O(n) to preprocess the magazine

class Solution:
    def __init__(self):
        # initializes a dict with all zeroes
        self.magazineDict = defaultdict(int)

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        self.preprocessMagazine(magazine)
        return self.checkRansomNote(ransomNote)


    def preprocessMagazine(self, mag: str) -> None:
        for char in mag:
            self.magazineDict[char] += 1

    def checkRansomNote(self, note: str) -> bool:
        for char in note:
            self.magazineDict[char] -= 1
            if self.magazineDict[char] < 0:
                return False
        return True

