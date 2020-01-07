# so many for loops, feels like i can do better with a map

class Solution:
    def commonChars(self, arr: [str]) -> [str]:
        if len(arr) == 0:
            return []

        buckets = [float('inf')] * 26

        for string in arr:
            tempBuckets = [0] * 26
            for ch in string:
                tempBuckets[ord(ch) - ord('a')] += 1
            for i in range(26):
                buckets[i] = min(buckets[i], tempBuckets[i])

        result = []
        occurences = zip(buckets, 'abcdefghijklmnopqrstuvwxyz')

        for bucket, ch in occurences:
            for _ in range(bucket):
                result.append(ch)
        return result









print(Solution().commonChars(["bella","label","roller"])) # ["e","l","l"]
print(Solution().commonChars(["cool","lock","cook"])) # ["c","o"]