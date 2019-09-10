// Generate all combinations, we can sorting the input string and running DFS.
// For each unique combination of letters, add the number of unique permutations.

// Runtime Complexit: for a string of size m, we will generate
// n! / (m! * (n - m)!) combinations, where n is the size of the input string.
// The complexity to calculate the number of permutations is O(m).
class Solution {
public:
    int numTilePossibilities(string tiles) {
        sort(begin(tiles), end(tiles));
        return dfs(tiles) - 1;
    }

private:
    // Pre-comuputed factories within given range
    static constexpr int fact[8] = { 1, 1, 2, 6, 24, 120, 720, 5040 };
    unordered_set<string> set;

    int uniquePerms(const string& s) {
        int freq[26] = {};
        for (auto& ch : s) {
            ++freq[ch - 'A'];
        }

        auto res = fact[s.size()];
        for (auto n : freq) {
            res /= fact[n];
        }
        return res;
    }

    int dfs(string& s, string seq = "", int pos = 0) {
    if (pos >= s.size()) {
        return set.insert(seq).second ? uniquePerms(seq) : 0;
    }
        return dfs(s, seq, pos + 1) + dfs(s, seq + s[pos], pos + 1);
    }
};


class Solution {
public:
    int numTilePossibilities(string tiles) {
        sort(tiles.begin(), tiles.end());
        int result = -1;
        helper(tiles, result, 0);
        
        return result;
    }

private:
   void helper(string tiles, int &result, int begin) {
        ++result;
        for (int i = begin; i < tiles.size(); ++i) {
            // Do not swap if it wouldnt not alter the string
            if (i != begin and tiles[i] == tiles[begin]) {
                continue;
            }
            // Check all unique permutations
            swap(tiles[i], tiles[begin]);
            helper(tiles, result, begin + 1);
        }
        return ;
    }
};