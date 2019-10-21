class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int val_if_hold = 0, val_if_buy = -INT_MAX;


        // val_if_hold = 7 <------

        //     val_if_buy = 3

        // new_val_if_hold = max(0, -inf + 7) = 0
        // new_val_if_hold = max(0, -7 + 1) = 0
        // new_val_if_hold = max(0, -1 + 5) = 4
        // new_val_if_hold = max(4, -1 + 3) = 4
        // new_val_if_hold = max(4, 1 + 6) = 7
        // new_val_if_hold = max(7, 1 + 4) = 7

        //     new_val_if_buy = max(-inf, 0 - 7) = -7
        //     new_val_if_buy = max(-7, 0 - 1) = -1
        //     new_val_if_buy = max(-1, 0 - 5) = -1
        //     new_val_if_buy = max(-1, 4 - 3) = 1
        //     new_val_if_buy = max(1, 4 - 6) = 1
        //     new_val_if_buy = max(1, 7 - 4) = 3
        for (int p : prices) {
            // hold if its not profitable to buy
            int new_val_if_hold = max(val_if_hold, val_if_buy + p);

            // buy if holding is less profitable
            int new_val_if_buy = max(val_if_buy, val_if_hold - p);
            val_if_hold = new_val_if_hold;
            val_if_buy = new_val_if_buy;
        }
        return val_if_hold;
    }
};