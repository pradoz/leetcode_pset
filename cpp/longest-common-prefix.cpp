class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) {
            return "";
        }
        for (int i = 1; true; ++i) {
            for (const string&  s : strs) {
                int end_of_prefix = i - 1;
                if (s.length() < i or s[end_of_prefix] != strs[0][end_of_prefix]) {
                    return s.substr(0, end_of_prefix);
                }
            }
        }
    }
};