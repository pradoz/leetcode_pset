#include <iostream>
#include<array>
#include<functional>

#include <vector>
using namespace std;


int main() {
    vector<int> vec = { 1,2,3,4,5,6,7,8,9 };

    sort(begin(vec), end(vec), [] (int a, int b) {
        return b > a;
    });

    for (auto item : vec) {
        cout << item << ' ';
    }

    return 0;
}