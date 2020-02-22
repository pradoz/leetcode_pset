// #include <iostream>
// #include <string>

// using namespace std;


class Solution {
public:
    string breakPalindrome(string palindrome) {
        const unsigned int size = palindrome.length();

        // trivial case
        // smallest bound on palindrome length is 1, so removing 1 character is
        // the empty string.
        if (size == 1) {
            return "";
        }

        // iterate over the string
        // note: size / 2 handles the odd case
        // ex: n = 5 / 2 = 2, so we don't care about the middle character because
        //      it could be anything and would still be a palindrome.
        for (unsigned int i = 0; i < size / 2; i++) {
            int j = size - 1 - i; // starts at back of string, moves to middle

            // iterate through the alphabet
            for (char ch = 'a'; ch <= 'z'; ch++) {
                if (palindrome[i] != 'a') {
                    palindrome[i] = ch;
                    return palindrome;
                }
            }
        }
        palindrome[size - 1] = 'b'; // edge case of "aa" --> "ab"
        return palindrome;



    }
};



// int main() {
//     Solution s = Solution();

//     cout << "s.breakPalindrome(\"abccba\"): "
//         << s.breakPalindrome("abccba") << endl;

//     cout << "s.breakPalindrome(\"aa\"): "
//         << s.breakPalindrome("aa") << endl;
//     return 0;
// }