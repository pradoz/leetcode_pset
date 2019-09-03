// Time Complexity: O(n*m), where n is the number of words, and m is the length
//                     length of the longest word of all n words.
// Space Complexity: O(1), this is constant because we only need to store ar
//                     mapping from each element to its corresponding index.

class Solution {
public:
    bool isAlienSorted(vector<string> &words, string order) {
        int mapping_arr[26]{};
        for (int i = 0; i < order.size(); ++i) {
            mapping_arr[order[i] - 'a'] = i;
        }
        // return is_sorted with lambda function as the key
        return is_sorted(words.begin(), words.end(), [&mapping_arr](
                const string &w1,
                const string &w2
        ) {
            int l1 = w1.size(), l2 = w2.size();
            for (int i = 0; i < min(l1, l2); ++i) {
                int c1 = w1[i], c2 = w2[i];
                if (c1 != c2) {
                    return mapping_arr[c1 - 'a'] < mapping_arr[c2 - 'a'];
                }
            }
            return l1 < l2;
        }); // end of call to is_sorted()
    }
};


// using unordered_map from STL
class Solution {
public:
    bool isAlienSorted(vector<string> &words, string order) {
        unordered_map<char, int> mapping;

        for(int i = 0; i < order.size(); i ++){
            mapping[order[i]] = i;
        }

        for (int i = 0; i < words.size() - 1; ++i) {
            int word_length = min(words[i].size(), words[i+1].size());

            for (int j = 0; j < word_length; ++j) {
                if (mapping[words[i][j]] == mapping[words[i+1][j]]) {
                    continue;
                }
                else if (mapping[words[i][j]] < mapping[words[i+1][j]]) {
                    break;
                }
                else { // (mapping[words[i][j]] > mapping[words[i+1][j]]) {
                    return false;
                }
            }
            if ((words[i+1].size() == word_length) and
                   (words[i].substr(0, word_length) == words[i+1])) {
                return false;
            }
        }
        return true;
    }
};