/*
Time complexity: O(m + n), since we traverse the magazine once to preprocess
                 it, and traverse the ransom note once to remove frequencies
                 from preprocessing.
Space complexity: O(n), since we store an occurrence of each character in the
                  magazine after we preprocess it.
*/

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        const int magazineLength = magazine.length();
        const int ransomNoteLength = ransomNote.length();

        // preprocess the magazine
        preprocess(magazine, magazineLength);
        return isValid(ransomNote, ransomNoteLength);
    }

private:
    unordered_map<char, int> magMap;
    void preprocess(const string& str, const int size) {
        for (int ch = 0; ch < size; ++ch) {
            magMap[str[ch]] += 1;
        }
        
    }

    bool isValid(const string& str, const int size) {
        for (int ch = 0; ch < size; ++ch) {
            magMap[str[ch]] -= 1;
            if (magMap[str[ch]] < 0) {
                return false;
            }
        }
        return true;
    }
};



class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        constexpr int bucketCount = 26;
        int chars[26] = {0};
        const int magazineLength = magazine.length();
        const int ransomNoteLength = ransomNote.length();

        // All letters are lowercase, substract 97 from their ASCIIto index them from 0-26
        for (int i = 0; i < magazineLength; ++i) {
            ++(chars[magazine[i] - 97]);
        }

        for (int i = 0; i < ransomNoteLength; ++i) {
            --(chars[ransomNote[i] - 97]);
        }

        for (int i = 0; i < bucketCount; ++i) {
            if (chars[i] < 0) {
                return false;
            }
        }
        return true;
    }
};






