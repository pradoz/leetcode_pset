class Solution {
public:
    int hammingDistance(int x, int y) {
        // __builtin_popcount returns the number of 1's in a values
        // binary representation.
        // XOR (^) returns a 1 if the bits are mismatched at the same index.
        return __builtin_popcount(x ^ y);
    }
};