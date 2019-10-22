class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        unordered_multiset<int> freqs;
        for (int n : nums1) {
            freqs.insert(n);
        }

        vector<int> result;
        for (int n : nums2) {
            if (freqs.count(n)) {
                result.push_back(n);
                freqs.erase(freqs.find(n));
            }
        }
        return result;
    }
};