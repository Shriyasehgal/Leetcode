class Codec:
    def __init__(self):
        self.encodeMap = {}
        self.count = 0
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.count += 1
        self.encodeMap[self.count] = longUrl
        return 'http://tinyurl.com/{}'.format(self.count)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        decode = shortUrl.split('/')[-1]
        return self.encodeMap[int(decode)]
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))