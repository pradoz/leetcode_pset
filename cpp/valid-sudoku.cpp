class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // We know the board is 9x9
        constexpr unsigned int H = 9;
        constexpr unsigned int W = 9;
        constexpr unsigned int SQ = 3; // 3x3 set of squares

        unordered_set<char> rows[W], cols[H], squares[SQ][SQ];

        for (int i = 0; i < H; ++i) {
            char ch = board[i][j];
            for (int j = 0; j < W; ++j) {
                if (ch != '.') {
                    if (!rows[i].insert(ch).second or
                        !cols[j].insert(ch).second or
                        !squares[i/SQ][j/SQ].insert(ch).second) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
};