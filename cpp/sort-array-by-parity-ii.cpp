// Naive solution, using O(1) space

// Invariant:
// arr[i] is an even number at even index and
// arr[j] is an odd number at odd index.
// As soon as this invariant is violated, we can swap numbers to restore it.

class Solution {
public:
    vector<int> sortArrayByParityII(vector<int>& arr) {
        int size = arr.size();
        for (int i = 0, j = 1; i < size and j < size; ) {
            if (arr[i] % 2 == 0) {
                i += 2;
            }
            else if (arr[j] % 2 == 1) {
                j += 2;
            }
            else {
                swap(arr[i], arr[j]);
            }
        }
        return arr;
    }
};


// Two pointer approach using O(1) space
class Solution {
public:
    vector<int> sortArrayByParityII(vector<int>& arr) {
        register int size = arr.size();
        for (int i = 0, j = 1; i < size; i += 2, j += 2) {
            while (i < size and arr[i] % 2 == 0) { i += 2; }
            while (j < size and arr[j] % 2 == 1) { j += 2; }
            if (i < size) { swap(arr[i], arr[j]); }
        }
        return arr;
    }
};