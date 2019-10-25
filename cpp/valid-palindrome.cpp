// Note: we can safely ignore case and assume alphanumeric input
class Solution {
public:
    bool isPalindrome(string s) {
        string only;

        for (char ch: s) {
            // Shift uppercase characters to lowercase
            if ('A' <= ch and ch <= 'Z') {
                ch += 'a' - 'A';
            }

            // append the character if it is alphanumeric
            if (isalnum(ch)) {
                only += ch;
            }
        }

        string tmp = only;
        reverse(tmp.begin(), tmp.end());

        return tmp == only;
    }
};