class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        const int HEIGHT = matrix.size();
        const int WIDTH = matrix[0].size();

        // Removing the vector of bools for rows reduces space complexity from
        // O(H+W) to O(W)
        // Removing col_of_zeroes, we reduce space complexity to O(1)
        // vector<bool> row_of_zeroes(HEIGHT);
        // vector<bool> col_of_zeroes(WIDTH);

        bool first_row_zero = false;
        for (int col = 0; col < WIDTH; ++col) {
            if (matrix[0][col] == 0) {
                first_row_zero = true;
            }
        }


        // set a flag that says the whole column should eventually
        // be filled with zeroes
        for (int row = 0; row < HEIGHT; ++row) {
            for (int col = 0; col < WIDTH; ++col) {
                if (matrix[row][col] == 0) {
                    // row_of_zeroes[row] = true;
                    // col_of_zeroes[col] = true;

                    
                    matrix[0][col] = 0;
                }
            }
        }

        // start iterating at the second row to preserve our flag values 
        for (int row = 1; row < HEIGHT; ++row) {
            bool row_contains_zero = false;
            for (int col = 0; col < WIDTH; ++col) {
                if (matrix[row][col] == 0) {
                    row_contains_zero = true;
                    break;
                }
            }
            for (int col = 0; col < WIDTH; ++col) {
                if (row_contains_zero or matrix[0][col] == 0) {
                    matrix[row][col] = 0;
                }
            }
        }

        // if we find the row zero flag, fill the first row with zeroes
        if (first_row_zero) {
            for (int col = 0; col < WIDTH; ++col) {
                matrix[0][col] = 0;
            }
        }
    }
};