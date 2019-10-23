class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        const int size = digits.size();

        reverse(digits.begin(), digits.end());

        // add one
        ++digits[0];
        for (int i = 0; i < digits.size(); ++i) {
            // if we have a carry
            if (digits[i] == 10) {
                // reset the digit
                digits[i] = 0;

                // if its the last digit, then push back another decimal place
                if (i == digits.size() - 1) {
                    digits.push_back(0);
                }

                // add the carry
                ++digits[i+1];
            }
        }
        reverse(digits.begin(), digits.end());

        return digits;
    }
};