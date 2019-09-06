/*
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
*/

// Using an unordered_map:
// Group strings if they match after being sorted alphabetically.
// The sorted string is the key and all anagrams that match when sorted
// are values.

// Time Complexity: O(n*m*log(m)) where n is the length of each word, and m
//                  is the length of each string we have to sort.
// Space Complexity: O(n*m) to store each word in the map.

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map;
        for (auto& str : strs) {
            string key = str;
            sort(key.begin(), key.end());
            map[key].push_back(str);
        }

        vector<vector<string>> anagrams;
        for (auto& m : map) {
            anagrams.push_back(m.second);
        }
        return anagrams;
    }
};


// Using counting sort:
// Time Complexity: O(n*m) where n is the size of the list, and m is the
//                  longest string in the list.
// Space Complexity: O(n*m) to store each word in the map.
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map;
        for (auto& str : strs) {
            map[counting_sort(str)].push_back(str);
        }

        vector<vector<string>> anagrams;
        for (auto& m : map) {
            anagrams.push_back(m.second);
        }
        return anagrams;
    }

private:
    string counting_sort(const string& s) {
        int counter[26] = {0};

        for (auto& c : s) {
            counter[c - 'a']++;
        }

        string key;
        for (int c = 0; c < 26; ++c) {
            key += string(counter[c], c + 'a');
        }
        return key;
    }
};