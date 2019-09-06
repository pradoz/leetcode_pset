'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''


'''
Solution Explanation:
Since there are at most 26 characters, we can keep count of all characters in
a tuple instead and save that as a key for the map.
'''

# Time Complexity: O(n*m) where n is the size of the list, and m is the longest
#                  string in the list.
# Space Complexity: O(n*m) to store each word in the map.

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            char_count = [0] * 26
            for c in s:
                char_count[ord(c) - ord('a')] += 1
            groups[tuple(char_count)].append(s)
        return list(groups.values())


'''
Solution Explanation:
If the words have the same sorted letters, we group them and store them
in a map. The values of the map are the solution.
'''

# Time Complexity: O(n*m*log(m)) where n is the length of each word, and m
#                  is the length of each string we have to sort.
# Space Complexity: O(n*m) to store each word in the map.

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            groups[''.join(sorted(s))].append(s)
        # print(groups)

        return list(groups.values())