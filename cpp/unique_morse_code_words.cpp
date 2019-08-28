#include <iostream>
#include <vector>
#include <unordered_set>
#include <string>
using namespace std;

// Fastest runtime approach
// hashing
class Solution {
public:
    int uniqueMorseRepresentations(vector<string>& words) {
        static const char* MORSE_CODE[] = {
            ".-","-...","-.-.","-..",".", "..-.","--.","....","..",".---",
            "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-",
            "...-",".--","-..-","-.--","--.."
        };
        unordered_set<string> hash;
        for (const auto word : words) {
            string encoded;
            for (int i = 0; i < word.size(); ++i)
                encoded += MORSE_CODE[word[i] - 'a'];

            // cout << encoded << endl;
            hash.insert(encoded);
        }

        return hash.size();
    }
};

int main() {
    Solution s1 = Solution();
    vector<string> words = {"gin", "zen", "gig", "msg"};
    cout << s1.uniqueMorseRepresentations(words);

    return 0;
}



