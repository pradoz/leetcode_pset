// We can assume that after we filled in all 0's and 1's,
// the remaining elements up to nums.end() will be filled in with the value 2.

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int c0 = 0;
        int c1 = 0;
        // We dont need this line below (it is commented out)
        // int c2 = 0;

        // Scan every number and count each occurrence of 0 or 1
        for (int num : nums) {
            switch (num) {
            case 0:
                ++c0;
                break;
            case 1:
                ++c1;
                break;
            // case 2:
            //     ++c2;
            //     break;
            }
        }

        // modify nums accordingly
        fill(nums.begin(), nums.begin() + c0, 0);
        fill(nums.begin() + c0, nums.begin() + c0 + c1, 1);
        fill(nums.begin() + c0 + c1, nums.end(), 2);
    }
};


// If we *assume* that the array is evenly distributed (has the same amount of 0's, 1's and 2's) we can see that when:
// i) n=6, there are k=2 2's in the vector, since 6/3 = 2 ( 3 is the amount of total colors )

// Above, we avoided 4 operations for each loop:
//   1. Checking the case where num is 2
//   2. Incrementing the integer
//   3. Assigning it
//   4. Break command to exit the switch statement

// which gives us 2*4=8 operations when n=6. Oh, and the initial variable declaration is 4 bytes and an extra assigment, so we end up with 8+1=9 total operations. 

// This may not seem like much at first, but if we consider a much larger value:
// ii) n=6000, there are k=2000 2's in the vector.

// In this case, we saved 2000*4+1 = 8001 total operations by avoiding extra work.

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int c0 = 0;
        int c1 = 0;
        // We dont need this line below (it is commented out)
        // int c2 = 0;

        // Scan every number and count each occurrence of 0 or 1
        for (int num : nums) {
            switch (num) {
            case 0:
                ++c0;
                break;
            case 1:
                ++c1;
                break;
            // case 2:
            //     ++c2;
            //     break;
            }
        }

        // modify nums accordingly
        fill(nums.begin(), nums.begin() + c0, 0);
        fill(nums.begin() + c0, nums.begin() + c0 + c1, 1);
        fill(nums.begin() + c0 + c1, nums.end(), 2);
    }
};


// One pass solution, use high (right side) and low (left side) pointers.
// Invariant: leave 1's in the middle, swap any 0's to the left and swap any
//            1's to the left.
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int left = 0;
        int curr = 0;
        int right = nums.size() - 1;

        // If curr == right, then we are done.
        while (curr <= right) {
            switch (nums[curr]) {
            case 0:
                // swap left with curr (using std::swap())
                swap(nums[left], nums[curr]);
                ++left;
                ++curr;
                break;
            case 2:
                // swap right with curr
                swap(nums[right], nums[curr]);
                --right;
                break;
            default:
                // advance if nums[curr] == 1
                ++curr;
            }
        }
    }
};



// Space efficient solution using a fixed-size array
class Solution {
public:
    int arr[3];
    int curr = 0;

    void color_array(int color, vector<int>& nums) {
        while (arr[color]--) {
            nums[curr++] = color;
        }
    }

    void sortColors(vector<int>& nums) {
        for (int num : nums) {
            arr[num]++;
        }
        color_array(0, nums);
        color_array(1, nums);
        color_array(2, nums);

    }

};