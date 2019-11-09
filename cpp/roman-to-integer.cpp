class Solution {
public:
    int romanToInt(string s) {
        int value = 0;
        int prev = 0;

        for (const char& c : s) {
            const int x = to_decimal(c);
            if (x <= prev) {
                value += prev;
                prev = x;
            }
            else {
                value -= prev;
                prev = x;
            }
        }
        return value + prev;
    }

private:
    const string letters = "IVXLCDM";
    const vector<int> numbers = {1, 5, 10, 50, 100, 500, 1000};
    const int num_letters = letters.size();

    // returns the decimal equivalent of a single roman numeral
    int to_decimal(const char& c) {
        for (int i = 0; i < num_letters; ++i) {
            if (letters[i] == c) {
                return numbers[i];
            }
        }
        assert(false);
    }
};