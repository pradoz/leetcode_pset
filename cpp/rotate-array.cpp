// Challenge: use O(1) space
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        k %= nums.size();

        // Reverse the entire array
        reverse(nums.begin(), nums.end());

        // Reverse the array from the front up to end-k
        reverse(nums.begin(), nums.begin() + k);

        // Reverse the last k elements of the array
        reverse(nums.begin() + k, nums.end());
    }
};