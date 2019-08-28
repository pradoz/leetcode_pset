#include <iostream>

int recursive_fib(int n) {
    if (n <= 1)
        return n;
    return recursive_fib(n-1) + recursive_fib(n-2);
}

int iterative_fib(int n) {
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

int main() {
    std::cout << recursive_fib(6) << std::endl;
    std::cout << recursive_fib(7) << std::endl;
    std::cout << recursive_fib(8) << std::endl;
    std::cout << iterative_fib(6) << std::endl;
    std::cout << iterative_fib(7) << std::endl;
    std::cout << iterative_fib(8) << std::endl;
    return 0;
}