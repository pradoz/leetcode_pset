# Count the number of prime numbers less than a non-negative number, n.
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

# Time complexity O(n) since we need to iterate through the array of booleans.
# Space complexity O(n) to create an array of booleans which has length of n.
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        indexIsPrimeNumber = [True] * n

        # Defaults
        indexIsPrimeNumber[0] = indexIsPrimeNumber[1] = False
        # indexIsPrimeNumber[2] = True

        # for idx in range(2, n):
        for idx in range(2, int(n ** 0.5) + 1):
            if indexIsPrimeNumber[idx] == True:
                nextMultiple = idx * 2
                while nextMultiple < n:
                    indexIsPrimeNumber[nextMultiple] = False
                    nextMultiple += idx


        listOfPrimes = []
        for num, isPrime in enumerate(indexIsPrimeNumber):
            if isPrime == True:
                listOfPrimes.append(num)

        return len(listOfPrimes)











print(Solution().countPrimes(10)) # 4