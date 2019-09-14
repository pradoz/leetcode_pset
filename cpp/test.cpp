#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
    vector<int> ret;
    vector<int> pos(26, 0);

    for (int i = 0; i < pos.size(); ++i) {
        pos.at(i) = i;
    }
    for (int i = 0; i < pos.size(); ++i) {
        if (i % 2 == 0) {
            exchange(0, i + 1);
        }
        cout << i << ": " << pos.at(i) << '\n';
    }
    // cout << 'a' - 'a' << endl;
    // cout << 'b' - 'a' << endl;
    // cout << 'c' - 'a' << endl;
    // cout << 'd' - 'a' << endl;

    return 0;
}