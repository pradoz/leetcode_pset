int fib(int n) {
    int f[n+2];
    f[0] = 0;
    f[1] = 1;

    for (int i = 2; i <= n; ++i) {
        f[i] = f[i-1] + f[i-2];
    }
    return f[n];
}


int fib(int n) {
    if (n < 2) return n;

    int prev = 0;
    int fib = 1;

    for (int i = 2; i <= n; ++i) {
        int hold_last = fib;
        fib += prev;
        prev = hold_last;
    }
    return fib;
}