#include <iostream>
#include <string>
#include <algorithm>
#include <cstddef>
using namespace std;

class Solution {
public:
    int longestPalindrome(string s) {
        int ret = 0;

        // count the frequencies in buckets
        int freq[255]{0};

        for (int ch : s) {
            // std::cout << "XXXX ch: " << static_cast<char>(ch) << "=" << ++freq[ch] << std::endl;
            ++freq[ch];
            // std::cout << freq[ch];
            // for (int i : freq) { std::cout << i;}
            // std::cout << std::endl;
        }

        bool found_an_odd = false;
        for (int i = 0; i < 255; ++i) {
            if (freq[i] % 2 == 1) {
                found_an_odd = true;
            }

            // Reduce the odd number, if possible, by c++ round-down int division
            ret += (freq[i]/2) * 2;
        }

        if (found_an_odd) {
            return ++ret;
        }


        return ret;
    }
};


class Solution0 {
public:
    int longestPalindrome(string s) {
        int use = 0;
        for (char c = 'A'; c <= 'z'; ++c) {
            // cout << "BEFORE - use= " << use << endl;
            use += count(s.begin(), s.end(), c) & ~1;
            // cout << "AFTER ~~ use= " << use << endl;
        }
        return use + (use < s.size());
    }
};

int main() {
    Solution s = Solution();
    cout << s.longestPalindrome("abccccdd") << endl;

    return 0;
}