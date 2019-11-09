class Solution {
public:
    bool isPowerOfThree(int n) {
        // if (n == 0) {
        //     return false;
        // }

        while (n > 4) {
            if (n % 3 != 0) {
                return false;
            }
            n /= 3;
        }
        return n == 1;
    }
};

// 2^(31) < 3^(20), and 1162261467 = 3^(19).
class Solution {
public:
    bool isPowerOfThree(int n) {
        return (n > 0 and 1162261467 % n == 0);
    }
};