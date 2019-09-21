/*
1. iterating left to right:
    - keep track of the maximum number
    - if the numbers that follow are smaller than the largest number, then
      sort those numbers so that right is set to that index at that point.

2. iterating right to left:
    - keep track of the minimum number
    - if the numbers that follow are greater than the smallest number, then
      those numbers need to be sorted so that left is set to that index at that
      point
*/

// Runs in O(n) since two traversals are required to process it all
// Uses O(1) "constant" space to store 4 integers and 1 constant integer

class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        // This algorithm is trivial for the empty vector and for vectors with
        // less than 2 elements, since they are already sorted.
        if (nums.empty() or nums.size() < 2) {
            return 0;
        }

        // It's possible to use O(n) space to check a sorted list here
        int start = 0;
        int finish = 0;
        const int size = nums.size();
        int max_num = nums.at(0);
        int min_num = nums.at(size - 1);

        // Get the end point
        for (int i = 1; i < size; ++i) {
            // Update the end point if necessary
            if (nums.at(i) < max_num) {
                finish = i;
            }

            max_num = max(max_num, nums.at(i));
        }

        // Get the start point
        for (int i = size - 1; i >= 0; --i) {
            // Update the end point if necessary
            if (nums.at(i) > min_num) {
                start = i;
            }

            min_num = min(min_num, nums.at(i));
        }
        return finish == start ? 0 : (finish - start + 1);
    }
};