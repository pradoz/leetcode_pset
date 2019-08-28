class Solution {
public:
    bool judgeCircle(string moves) {
        ios_base::sync_with_stdio(false); cin.tie(nullptr); // random performance line
        if (moves == "")
            return true;

        int ud_count = 0;
        int lr_count = 0;

        for (const char move : moves) {
            if (move == 'U') ++ud_count;
            else if (move == 'D') --ud_count;
            else if (move == 'L') ++lr_count;
            else --lr_count; // (move == 'R')
        }

        return (ud_count == 0 and lr_count == 0);
    }
};

class Solution {
public:
    bool judgeCircle(string moves) {
        ios_base::sync_with_stdio(false); cin.tie(nullptr); // random performance line
        if (moves == "")
            return true;

        int up_count = count(moves.begin(), moves.end(), 'U');
        int down_count = count(moves.begin(), moves.end(), 'D');
        int left_count = count(moves.begin(), moves.end(), 'L');
        int right_count = count(moves.begin(), moves.end(), 'R');

        if (up_count == down_count and left_count == right_count)
            return true;
        return false;
    }

};
