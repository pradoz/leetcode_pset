class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int val_if_hold = 0, val_if_buy = -INT_MAX;

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