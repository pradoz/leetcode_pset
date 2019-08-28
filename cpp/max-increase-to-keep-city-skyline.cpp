/*
Example:
Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
Output: 35
Explanation: 
The grid is:
[ [3, 0, 8, 4], 
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]

The skyline viewed from top or bottom is: [9, 4, 8, 7]
The skyline viewed from left or right is: [8, 7, 9, 3]

The grid after increasing the height of buildings without affecting skylines is:

gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]
*/

class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        // If the grid were M by N, then we would need to keep track of two
        // sizes to avoid going out of bounds on j.

        // Since this "city" is N by N, we only need one size.
        const int sz = grid.size();
        int* top_skyline = new int[sz]{INT_MIN};
        int* side_skyline = new int[sz]{INT_MIN};
        // vector<int> top_skyline(sz, 0), side_skyline(sz, 0);


        for (int i = 0; i < sz; ++i) {
            for (int j = 0; j < sz; ++j) {
                int grid_location = grid[i][j];
                if (top_skyline[i] < grid_location) {
                    top_skyline[i] = grid_location;
                }
                if (side_skyline[j] < grid_location) {
                    side_skyline[j] = grid_location;
                }
            }
        }

        int total = 0;
        for (int i = 0; i < sz; ++i) {
            for (int j = 0; j < sz; ++j) {
                total += !(side_skyline[j] < top_skyline[i])
                         ? top_skyline[i] - grid[i][j]
                         : side_skyline[j] - grid[i][j];

                // if (top_skyline[i] <= side_skyline[j]) {
                //     total += top_skyline[i] - grid[i][j];
                // }
                // else {
                //     total += side_skyline[j] - grid[i][j];
                // }
                // total += min(top_skyline[i], side_skyline[j]) - grid[i][j];
            }
        }

        delete[] top_skyline;
        delete[] side_skyline;

        return total;
    }
};

