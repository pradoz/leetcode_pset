// quadratic runtime, constant space
class Solution {
public:
    string longestPalindrome(string s) {
        int bestLength = 0;
        string bestString = "";

        const int size = s.length();

        // middle-out aglorithm lol
        for (int mid = 0; mid < size; ++mid) {
            for (int x = 0; mid - x >= 0 and mid + x < size; ++x) { 
                if (s[mid - x] != s[x + mid]) {
                    break; // not a palindrome
                }
                // if we didn't break, then we have a palindrome which spans
                // from the mid character plus two character substrings of 
                // length x to the left and right of the mid character.
                int length = 2 * x + 1;
                if (length > bestLength) {
                    bestLength = length;
                    bestString = s.substr(mid - x, length);
                }
            }
        }

        // odd length string case
        for (int mid = 0; mid < size - 1; ++mid) {
            for (int x = 1; mid - x + 1 >= 0 and mid + x < size; ++x) {
                if (s[mid - x + 1] != s[x + mid]) {
                    break; // not a palindrome
                }
                int length = 2 * x;
                if (length > bestLength) {
                    bestLength = length;
                    bestString = s.substr(mid - x + 1, length);
                }
            }
        }

        return bestString;
    }
};