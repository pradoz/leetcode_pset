// This ended up being the best space solution
// (even over the very similar one with ternary op.)
class Solution {
public:
    int trap(vector<int>& heights) {
        if (heights.size() < 3) { return 0; }
        int left = 0, right = heights.size() - 1, level = 0, water = 0, lower = 0;

        while (left < right) {
            if (heights[left] < heights[right]) {
                lower = heights[left++];
            }
            else {
                lower = heights[right--];
            }
            level = max(level, lower);
            water += level - lower;
        }
        return water;
    }
};

// Ridiculous ternary operation in the subscript operator
class Solution {
public:
    int trap(vector<int>& heights) {
        if (heights.size() < 3) { return 0; }
        int left = 0, right = heights.size() - 1, level = 0, water = 0;

        while (left < right) {
            int lower = heights[heights[left] < heights[right] ? left++ : right--];
            level = max(level, lower);
            water += level - lower;
        }
        return water;
    }
};

// With iterators
class Solution {
public:
    int trap(vector<int>& heights) {
        if (heights.size() < 3) { return 0; }
        auto left = heights.begin(), right = heights.end() - 1;
        int level = 0, water = 0;

        while (left != right) {
            int lower = *left < *right ? *left++ : *right--;
            level = max(level, lower);
            water += level - lower;
        }
        return water;
    }
};