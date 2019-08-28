'''
Example 1:
Input: J = "aA", S = "aAAbbbb"
Output: 3

Example 2:
Input: J = "z", S = "ZZ"
Output: 0
'''
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        J = set(J)
        jewel_count = 0
        for i in range(len(S)):
            if S[i] in J:
                jewel_count += 1
        return jewel_count



def main():
    s1 = Solution()
    s1.numJewelsInStones('aA', 'aAAbbbb')
    s1.numJewelsInStones('z', 'ZZ')
    assert s1.numJewelsInStones('aA', 'aAAbbbb') == 3
    assert s1.numJewelsInStones('z', 'ZZ') == 0

if __name__ == '__main__':
    main()