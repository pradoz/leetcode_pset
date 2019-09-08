// Time Complexity: O(n), since work is done in a linear pass
// Space Complexity: O(n), since we store every character in the list


// Brute-force Solution: reverse every string individually, then concatenate
//      them before returning.
class Solution {
public:
    string reverseWords(string s) {
        int front_of_word = 0;
        for (int i = 0; i <= s.length(); ++i) {
            if (i == s.length() or s[i] == ' ') {
                reverse(&s[front_of_word], &s[i]);
                front_of_word = i + 1;
            }
        }
        return s;
    }
};


// Less built in function Solution: swap the letters at the front and
// back of the string, do not swap if characters match.
class Solution {
public:
    string reverseWords(string s) {
        int front_of_word = 0;
        int whitespace_idx = 0;
        static constexpr int sz = s.length();

        while (whitespace_idx < sz) {
            // Find the next whitespace index
            while (whitespace_idx < sz and s[whitespace_idx] != ' ') {
                ++whitespace_idx;
            }

            // Get current word size
            int curr_word_size = whitespace_idx - 1;

            // Reverse the current word
            while (front_of_word < curr_word_size) {
                swap(s[front_of_word++], s[curr_word_size--]);
                // ++front_of_word;
                // --curr_word_size;

            }
            // Update whitespace_idx index
            front_of_word = ++whitespace_idx;
        }
        return s;
    }
};


// Neat solution using istringstream. Simply read in each word backwards.
class Solution {
public:
    string reverseWords(string s) {
        istringstream iss{s};
        auto itr = s.begin();

        for (string word; iss >> word; ) {
            itr = copy(word.rbegin(), word.rend(), itr);

            if (itr != s.end()) {
                ++itr;
            }
        }
        return s;
    }
};