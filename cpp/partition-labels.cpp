/*
A string S of lowercase letters is given. We want to partition this string
into as many parts as possible so that each letter appears in at most one part,
and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it
splits S into less parts.
*/

// On the first pass, we record the last position of each letter.
// On the second pass, keep the max position of each letter we've seen.
// Runs in linear time in two passes, uses constant space to store 26 elements.
class Solution {
public:
    vector <int> partitionLabels(string S) {
        vector<int> ret;
        vector<int> pos(26, 0);

        for (int i = 0; i < S.size(); ++i) {
            pos[S[i] - 'a'] = i;
        }
        for (int i = 0, max_idx = INT_MIN, last_max_idx = 0; i < S.size(); ++i) {
            max_idx = max_idx(idx, pos[S[i] - 'a']);
            if (max_idx == i) {
                ret.push_back(i - exchange(last_max_idx, i + 1) + 1);
            }
        }
        return ret;
    }
};
