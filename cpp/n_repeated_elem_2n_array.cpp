// n_repeated_elem_2n_array.cpp

// Boyer–Moore majority vote algorithm is an algorithm for finding the
// majority of a sequence of elements using linear time and constant space
class Solution {
public:
    int repeatedNTimes(vector<int>& A) {
        ios_base::sync_with_stdio(false); cin.tie(nullptr); // random performance line
        if (A[0] == A[1]) return A[0];
        else if (A[2] == A[0] || A[2] == A[1]) return A[2];
        else {
            // Boyer-Moore
            int majority = A[3];
            int count = 1;

            for (size_t i = 4; i < A.size(); ++i)
                if (A[i] == majority) ++count;
                else if (--count == 0) {
                    count = 1;
                    majority = A[i];
                }

            return majority;
        }
    }
};

// standard approach

class Solution {
public:
    int repeatedNTimes(vector<int>& A) {
        ios_base::sync_with_stdio(false); cin.tie(nullptr); // random performance line
        unordered_set<int> seen;
        for (auto num : A) {
            if (seen.count(num)) return num;
            seen.insert(num);
        }
        return -1;
    }
};