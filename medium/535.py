# https://leetcode.com/problems/encode-and-decode-tinyurl/

import random

class Codec:
    def __init__(self):
        self.urls = {}
    
    def encode(self, longUrl):
        while True:
            ran = []
            a2z = [chr(i) for i in range(ord('a'), ord('z')+1)]
            zero2nine = list(map(str,range(0,10)))
            ran = a2z + zero2nine

            url = 'http://tinyurl.com/' + ''.join(random.choices(ran, k=6))
            if url in self.urls.keys():
                continue
            self.urls[url] = longUrl
            # print(f'Encode: {url}')
            return url

    def decode(self, shortUrl):
        if shortUrl in self.urls.keys():
            # print(f'Decode: {self.urls[shortUrl]}')
            return self.urls[shortUrl]
        return False
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))


