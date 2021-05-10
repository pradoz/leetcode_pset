from typing import List

# O(n*k) time
# O(k) space -- k is the number of allowed characters
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result = 0
        allowed_set = set(allowed)

        for i, word in enumerate(words):
            j = 0
            k = len(word)
            while j <= k:
                if j == k:
                    result += 1
                    break

                # check if the next character is consisent
                ch = word[j]
                if ch not in allowed_set:
                    break
                j += 1

        return result




allowed = ['ab', 'abc', 'cad']
words = [
        ["ad","bd","aaab","baa","badab"],
        ["a","b","c","ab","ac","bc","abc"],
        ["cc","acd","b","ba","bac","bad","ac","d"],
        ]

test_results = [2,7,4]
test_cases = len(test_results)

def run_test() -> None:
    sol = Solution()
    for i in range (test_cases):
        check_test = sol.countConsistentStrings(allowed[i], words[i])
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
