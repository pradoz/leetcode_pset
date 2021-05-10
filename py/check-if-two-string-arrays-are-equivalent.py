from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1 = ''.join(word1)
        s2 = ''.join(word2)

        n = len(s1)
        m = len(s2)
        if n != m:
            return False

        for i in range(n):
            if s1[i] != s2[i]:
                return False

        return True




word1 = [["ab", "c"],["a", "cb"],["abc", "d", "defg"], ["ab", "c"]]
word2 = [["a", "bc"], ["ab", "c"], ["abcddefg"], ["a", "bc"]]

test_results = [True, False, True, True]
test_cases = len(test_results)

def run_test() -> None:
    sol = Solution()
    for i in range (test_cases):
        check_test = sol.arrayStringsAreEqual(word1[i], word2[i])
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
