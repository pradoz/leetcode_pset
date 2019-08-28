#include <iostream>
#include <vector>
using namespace std;
int peakIndexInMountainArray(vector<int>& A) {
    int idx = 0;
    while (idx < A.size()-1)  {
        if (A[idx] > A[idx+1]) {
            return A[idx];
        }
        ++idx;
    }
    return A[idx];
}

vector<int> vec = {3, 4, 5, 1};

// cout << peakIndexInMountainArray(vec) << endl;