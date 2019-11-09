class Solution {
public:
    int hammingWeight(uint32_t n) {
        // Returns the number of 1's in the two's complement binary
        // representation of n.
        return __builtin_popcount(n);
    }
};