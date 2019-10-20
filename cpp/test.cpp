#include <iostream>

#include <vector>
using namespace std;


int main() {
    const int H = 3;
    const int W = 5;
    vector<vector<int>> matrix(H, vector<int>(W));

    for (int row = 0; row < H; ++row) {
        cout << '[';
        for (int col = 0; col < W; ++col) {
            matrix[row][col] = 1;
            cout << matrix[row][col] << ", ";
        }
        cout << ']' << endl;
    }
    cout << "\n\n";

    for (int row = 0; row < H; ++row) {
        for (int col = 0; col < W; ++col) {
            matrix[row][0] = 0;
        }
    }

    // cout << "\n\n";
    for (int row = 0; row < H; ++row) {
        cout << '[';
        for (int col = 0; col < W; ++col) {
            cout << matrix[row][col] << ", ";
        }
        cout << ']' << endl;
    }


    return 0;
}