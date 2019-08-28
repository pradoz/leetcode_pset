# Recursively
class Solution0:
    def longestSubstring(self, s: str, k: int) -> int:
        size_of_string = len(s)
        if len(s) < k:
            return 0
        for c in set(s):
            print(f'entering for loop... c={c}')
            if s.count(c) < k:
                # print(f'entering for loop... self.longestSubstring(z, k) for z in s.split(c)={self.longestSubstring(z, k) for z in s.split(c)}')
                return max(self.longestSubstring(z, k) for z in s.split(c))
        return len(s)


# Iteratively with a stack
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        stack = []
        stack.append(s)
        ans = 0
        while stack:
            s = stack.pop()
            # print(f's={s}')
            for c in set(s):
                # print(f'---------- c={c}, s.count(c): {s.count(c)}')
                if s.count(c) < k:
                    # print("1:", stack)
                    stack.extend([z for z in s.split(c)])
                    # print("2:", stack)
                    break
            else:
                # print("ans len(s) = ", ans, len(s))
                ans = max(ans, len(s))
        return ans



# Iteratively, using the alphabets range
class Solution2:
    def longestSubstring(self, s: str, k: int) -> int:
        ans = 0
        for n in range(1, 27): # [1, 27)
            l = 0
            counter = {}
            for r in range(len(s)):
                if s[r] not in counter:
                    counter[s[r]] = 0
                counter[s[r]] += 1

                while len(counter) > n:
                    counter[s[l]] -= 1
                    if counter[s[l]] == 0:
                        counter.pop(s[l])

                    l += 1

                if all([z >= k for z in counter.values()]):
                    ans = max(ans, r - l + 1)
        return ans











print(Solution().longestSubstring("aaabb", 3)) # 3
print(Solution().longestSubstring("ababbc", 2)) # 5














