'''
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
'''

import random
import string
class Codec:
    def __init__(self):
        self.mapping = {}
        self.available = string.printable
    
    def encode(self, longUrl):
        ext = ''.join(random.sample(self.available, k=2))
        self.mapping[ext] = longUrl
        return "http://tinyurl.com/"+ext
        
    def decode(self, shortUrl):
        return self.mapping[shortUrl[-2:]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
