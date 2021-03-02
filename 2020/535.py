'''
535
'''
import random
import string
class Codec:
    self.urlDict = {}
    self.urlDict['a'] = 'a'
    self.pool = string.ascii_letters + string.digits
    def encode(self, longUrl: str) -> str:
        """
        Encodes a URL to a shortened URL.
        """
        shortUrl = 'a'
        while shortUrl in self.urlDict:
            shortUrl = ''.join(random.choice(self.pool) for _ in range(7))
        self.urlDict[shortUrl] = longUrl
        return 'http://tinyurl.com/'+shortUrl
        

    def decode(self, shortUrl: str) -> str:
        """
        Decodes a shortened URL to its original URL.
        """
        return self.urlDict[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))