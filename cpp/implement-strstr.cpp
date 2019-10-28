class Solution {
public:
    int strStr(string haystack, string needle) {
        const int haystack_size = haystack.length() - needle.length() + 1;
        const int needle_size = needle.length();

        // iterate over the haystack up the the point at which the needle might
        // still be present
        for (int i = 0; i < haystack_size; ++i) {
            // check if the needle is in the haystack
            if (needle == haystack.substr(i, needle_size)) {
                return i;
            }
        }
        return -1;
    }
};