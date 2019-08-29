class Codec:
    def __init__(self):
        # O(n) extra space used to store n urls.
        self.hash_dict = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        # get the hashed value in string form
        hash_id = str(self.longUrlToId(longUrl))

        # store the longUrl in the hash dict at its computed id
        self.hash_dict[hash_id] = longUrl
        return "http://tinyurl.com/" + hash_id

    # O(k), where k is the characters after the original url
    def longUrlToId(self, url):
        id_val = 0
        # hash function for id (hash index where url is stored to decode)
        for ch in url:
            id_val = (id_val * 62 + ord(ch)) % 100000
        return id_val
        
    # decode runs in O(1)
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        # get the part of the url after the last slash found
        hashed_val = shortUrl.split('/')[-1]
        return self.hash_dict[hashed_val]


# simple counter
class Codec1:
    def __init__(self):
        self.urls = []

    def encode(self, longUrl):
        self.urls.append(longUrl)
        return 'http://tinyurl.com/' + str(len(self.urls) - 1)

    def decode(self, shortUrl):
        return self.urls[int(shortUrl.split('/')[-1])]



# Your Codec object will be instantiated and called as such:
codec = Codec()
url = "https://leetcode.com/problems/design-tinyurl"

print(codec.encode(url))
encoded_url = codec.encode(url)
print(codec.decode(encoded_url))

print(codec.decode(codec.encode(url)))