// recursive, inefficient/no memoization
class Solution {
public:
    int fib(int n) {
        if (n <= 1)
            return n;
        return fib(n-1) + fib(n-2);
    }
};


// dynamic programming solution
class Solution {
public:
    int fib(int n) {
        vector<int> f(n+2);
        f[0] = 0; f[1] = 1;

        for (int i = 2; i <= n; ++i) {
            f[i] = f[i-1] + f[i-2];
        }
        return f[n];
    }
};


// iterative, O(n)
class Solution {
public:
    int fib(int n) {
    if (n <= 1)
        return n;

        int prev = 1;
        int fib = 1;

        for (int i = 2; i < n; ++i) {
            int temp = fib;
            fib += prev;
            prev = temp;
        }
        return fib;
    }
};




