#include <chrono>
#include <iostream>
using namespace std;
// hamming-distance.cpp

/* Note:
 * The builtin function has close performance to the bitmask version, and is
    much more readable.
*/


int hammingDistance1(int x, int y) {
    x ^= y;
    x = (x & 0x55555555) + ((x>>1) & 0x55555555);
    x = (x & 0x33333333) + ((x>>2) & 0x33333333);
    x = (x & 0x0F0F0F0F) + ((x>>4) & 0x0F0F0F0F);
    x = (x & 0x00FF00FF) + ((x>>8) & 0x00FF00FF);
    x = (x & 0x0000FFFF) + ((x>>16) & 0x0000FFFF);
    return x;
}

// helper function
bool ison (int x,int i ) {
    if(x&(1<<i))
        return true;
    return false;
}
int hammingDistance2(int x, int y) {
    int m  = max(x,y);
    int bt =0;
    int ans =0;
    while (bt<32 && (1<<bt)<=m) {
        if ( (ison(x,bt) && !ison(y,bt)) ||(!ison(x,bt) && ison(y,bt)) )
            ans++;
        bt++;
    }
    return ans;
}


int hammingDistance3(int x, int y) {
    return __builtin_popcount(x^y);
}

int main() {
    // C++11
    chrono::steady_clock::time_point begin1 = chrono::steady_clock::now();
    hammingDistance1(8171, 1073741773);
    chrono::steady_clock::time_point end1 = chrono::steady_clock::now();
    double t1 = chrono::duration_cast<chrono::nanoseconds>(end1 - begin1).count();
    cout << "(Hexadec) Total Time Elapsed: " << t1 << " nanoseconds" << endl;

    chrono::steady_clock::time_point begin2 = chrono::steady_clock::now();
    hammingDistance2(8171, 1073741773);
    chrono::steady_clock::time_point end2 = chrono::steady_clock::now();
    double t2 = chrono::duration_cast<chrono::nanoseconds>(end2 - begin2).count();
    cout << "(funhelp) Total Time Elapsed: " << t2 << " nanoseconds" << endl;

    chrono::steady_clock::time_point begin3 = chrono::steady_clock::now();
    hammingDistance3(8171, 1073741773);
    chrono::steady_clock::time_point end3 = chrono::steady_clock::now();
    double t3 = chrono::duration_cast<chrono::nanoseconds>(end3 - begin3).count();
    cout << "(builtin) Total Time Elapsed: " << t3 << " nanoseconds" << endl;


    return 0;
}