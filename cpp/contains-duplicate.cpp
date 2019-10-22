class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> set_of_nums;
        for (int n : nums) {
            set_of_nums.insert(n);
        }

        return nums.size() > set_of_nums.size();
    }
};