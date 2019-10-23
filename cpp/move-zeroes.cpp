// Challenge: must be done in-place
// Challenge: minimize total operations

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int zero_idx = 0;

        for (int x : nums) {
            if (x != 0) {
                nums[zero_idx] = x;
                ++zero_idx;
            }
        }

        for (int i = zero_idx; i < nums.size(); ++i) {
            nums[i] = 0;
        }
    }
};