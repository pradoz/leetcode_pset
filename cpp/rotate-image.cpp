// Note: Must be done in-place. Do not allocate another 2d matrix
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        // Since the matrix is NxN, only need to store one size
        const int size = matrix.size();

        for (int i = 0; i < (size / 2); ++i) {
            for (int j = 0; j < (size + 1) / 2; ++j) {
                int prev = matrix[i][j];
                for (int rep = 0; rep < 4; ++rep) {
                    int new_i = j;
                    int new_j = size - 1 - i;
                    int temp = matrix[new_i][new_j];

                    matrix[new_i][new_j] = prev;
                    prev = temp;
                    i = new_i;
                    j = new_j;
                }
            }
        }
    }
};