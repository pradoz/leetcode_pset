class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = [x for x in 'abcdefghijklmnopqrstuvwxyz']
        count = 0

        for ch in sentence:
            idx = ord(ch) - ord('a')
            if alphabet[idx] != '#':
                alphabet[idx] = '#'
                count += 1

        return True if count > 25 else False

class Solution1:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = {x for x in 'abcdefghijklmnopqrstuvwxyz'}
        for ch in sentence:
            if ch in alphabet:
                alphabet.remove(ch)

        return not alphabet


# O(n) / O(1)
class Solution0:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = {letter: False for letter in 'abcdefghijklmnopqrstuvwxyz'}

        for ch in sentence:
            seen[ch] = True

        for val in seen.values():
            if val == False:
                return False
        return True





sentence = ["thequickbrownfoxjumpsoverthelazydog", "leetcode"]

test_results = [True, False]
test_cases = len(test_results)

def run_test() -> None:
    sol = Solution()
    for i in range (test_cases):
        check_test = sol.checkIfPangram(sentence[i])
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
