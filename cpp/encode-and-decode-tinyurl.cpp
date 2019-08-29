// using unordered maps
class Solution {
public:
    // Encodes a URL to a shortened URL.
    string encode(string longUrl) {
        // if we can't find longUrl, add it to the map
        if (orgToEnc.find(longUrl) != orgToEnc.end()) {
            return orgToEnc[longUrl];
        }

        // compute hash
        string key = "";
        for (int i = 0; i < 6; ++i) {
            key += alphabet[rand() % alphabet.length()];
        }

        string shortUrl = "http://tinyurl.com" + key;
        orgToEnc[longUrl] = shortUrl;
        encToOrg[shortUrl] = longUrl;

        return shortUrl;
    }

    // Decodes a shortened URL to its original URL.
    string decode(string shortUrl) {
        return encToOrg[shortUrl];
    }
    
private:
    unordered_map<string, string> orgToEnc;
    unordered_map<string, string> encToOrg;
    string alphabet = "abcdefghijklmnoprsuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
};



// by size
class Solution {
public:
    // Encodes a URL to a shortened URL.
    string encode(string longUrl) {
        urls.push_back(longUrl);
        return to_string(urls.size() - 1);
    }

    // Decodes a shortened URL to its original URL.
    string decode(string shortUrl) {
        return urls.at(stoi(shortUrl));
    }
    
private:
    vector<string> urls;
};

// Your Solution object will be instantiated and called as such:
// Solution solution;
// solution.decode(solution.encode(url));