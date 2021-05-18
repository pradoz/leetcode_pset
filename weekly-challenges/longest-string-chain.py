from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        memo = {}

        # sort words with ascending lengths
        words.sort(key=lambda x: len(x))

        max_chain = 0
        for word in words:
            longest = 0
            for i in range(len(word)):
                # check each word with the i^th character missing
                check = word[:i] + word[i+1:]
                longest = max(longest, memo.get(check, 0) + 1)

            memo[word] = longest
            max_chain = max(max_chain, longest)
        return max_chain








words = [["a","b","ba","bca","bda","bdca"], ["xbc","pcxbcf","xb","cxbc","pcxbc"]]

test_results = [4, 5]
test_cases = len(test_results)

def run_test() -> None:
    sol = Solution()
    for i in range (test_cases):
        check_test = sol.longestStrChain(words[i])
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
