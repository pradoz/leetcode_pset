// Linear search
class Solution {
public:
    int peakIndexInMountainArray(vector<int>& A) {
        ios_base::sync_with_stdio(false); cin.tie(nullptr); // random performance line
        int idx = 0;
        while (idx < A.size()-1)  {
            if (A[idx] > A[idx+1]) {
                return idx;
            }
            ++idx;
        }
        return idx;
    }

};

// Binary search
class Solution {
public:
    int peakIndexInMountainArray(vector<int>& A) {
        ios_base::sync_with_stdio(false); cin.tie(nullptr); // random performance line

        int front = 0;
        int back = A.size() - 1;

        while (front < back) {
            int mid = (front + back) / 2;
            if (A[mid] < A[mid+1])
                front = mid + 1;
            else
                back = mid;
        }
        return front;
    }
};


// Ternary search?
class Solution {
public:
    int peakIndexInMountainArray(vector<int>& A) {
        int low = 0;
        int high = A.size() - 1;

        while (high - low >= 3) {
            int mid1 = low + (high - low)/3;
            int mid2 = high - (high - low)/3;
            if (A[mid1] < A[mid2]) {
                low = mid1;
            }
            else if (A[mid1] > A[mid2]) {
                high = mid2;
            }
            else if (A[mid1] == A[mid2]) {
                low = mid1;
                high = mid2;
            }
        }

        int res = A[low];
        int idx = low;
        while (low <= high) {
            if (A[low] > res) {
                res = A[low];
                idx = low;
            }
            ++low;
        }
        return idx;
    }
};


class Solution {
public:
    int peakIndexInMountainArray(vector<int>& A) {
        ios_base::sync_with_stdio(false); cin.tie(nullptr); // random performance line
        const int size = A.size() - 1;
        int i = 0;
        int j = 0;
        while(i < size) {
            if(A[i] > A[i+1]) {
                j = i;
                break;
            }
            ++i;
        }
        return j;
    }
};


class Solution {
public:
    int peakIndexInMountainArray(vector<int>& A) {
        ios_base::sync_with_stdio(false); cin.tie(nullptr); // random performance line
        for (auto itr = A.begin(); itr != A.end()-1; ++itr) {
            if (itr > itr+1)
                return itr;
        }
    }
};

