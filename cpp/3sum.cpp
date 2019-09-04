/*
Solution Explanation:
First we should sort nums, iterate through every number in nums, using the
current number as a target value which can be reached obtaining a larger or
smaller number by incrementing the left pointer or decrementing the right
pointer, respectively.

Time Complexity: O(n^2)
Space Complexity: O(n)
*/

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> results;
        sort(nums.begin(), nums.end());
        int size = nums.size();

        // Exit early cases:
        // 1. If the list has less than 3 elements.
        // 2. If the first element is positive in an increasingly sorted list,
        //    then their sum will always be greater than zero.
        // 3. If the last element is negative in the increasingly sorted list,
        //    then we have the converse of case 2.
        if (size < 3 or nums.front() > 0 or nums.back() < 0) {
            return {}; // Return empty vector, no 3sum can possibly exist.
        }

        // This algorithm requires 3 nums to run, so stop at nums.size()-2
        for (int i = 0; i < nums.size() - 2; ++i) {
            // Avoid checking duplicate elements, "continue" takes us back to
            // the conditional part of the for loop, then its body if true.
            if (i > 0 and nums[i] == nums[i-1]) {
                continue;
            }

            // Left and right pointers
            int left = i + 1;
            int right = size - 1;
            int total = 0;

            while (left < right) {
                total = nums[i] + nums[left] + nums[right];

                // If the total is greater than zero, we need to move the right
                // pointer to the left to get a smaller number.
                if (total < 0) { ++left; }
                else if (total > 0) { --right; }
                else {
                    results.push_back({nums[i], nums[left], nums[right]});
                    while (left < right and nums[left] == nums[left + 1]) {
                        ++left;
                    }
                    while (left < right and nums[right] == nums[right - 1]) {
                        --right;
                    }
                    ++left;
                    --right;
                }
            }
        }
        return results;
    }
};




// Solution using another solution to the two-sum problem