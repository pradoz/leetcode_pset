from math import sqrt

# O(n) time and space -- naive Sieve of Eratosthenes
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 1:
            return 0
        sieve = [True] * n

        for i in range(2, int(sqrt(n)) + 1):
            if sieve[i] == True:
                # j = i ** 2
                # while j < n:
                for j in range(i ** 2, n, i):
                    sieve[j] = False
                    # j += i
        result = 0
        for i in range(2, n):
            if sieve[i] == True:
                result += 1

        return result








n= [10, 0, -1, 18]

test_results = [4, 0, 0, 7]
test_cases = len(test_results)

def run_test() -> None:
    sol = Solution()
    for i in range (test_cases):
        check_test = sol.countPrimes(n[i])
        test_flag = True if check_test == test_results[i] else False
        if test_flag == True:
            print(f'++++ TEST #{i+1}: SUCCESS. Result = {check_test}')
        else:
            print(f'---- TEST #{i+1}: FAILURE.')
            print(f'       Expected: {test_results[i]}')
            print(f'       Received: {check_test}')

def main() -> None:
    run_test()

if __name__ == '__main__':
    main()
